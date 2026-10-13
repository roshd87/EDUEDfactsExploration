param(
  [int]$Port = 9223,
  [string]$OutRoot = 'C:\Repos\EDUEDfacts\wiki\reference\edfacts\2026-27\_inbox',
  [string[]]$Pages = @(
    'https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-file-specifications/edfacts-file-specifications-sy-2026-27',
    'https://www.ed.gov/data/edfacts-initiative/edfacts-resources',
    'https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-business-rules',
    'https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-workbook',
    'https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edpass-metadata-documentation',
    'https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edpass-general-documentation'
  ),
  [switch]$CloseBrowser,
  [int]$DelayMs = 0,
  [int]$CoolDownSec = 0
)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
Add-Type -AssemblyName System.Web.Extensions
$ser = New-Object System.Web.Script.Serialization.JavaScriptSerializer
$ser.MaxJsonLength = [int]::MaxValue

$targets = Invoke-RestMethod "http://127.0.0.1:$Port/json"
$page = $targets | Where-Object { $_.type -eq 'page' } | Select-Object -First 1
if (-not $page) { throw 'no page target' }
$ws = New-Object System.Net.WebSockets.ClientWebSocket
$ws.ConnectAsync([Uri]$page.webSocketDebuggerUrl, [Threading.CancellationToken]::None).Wait()
$script:msgId = 0

function Send-Msg($obj) {
  $json = $ser.Serialize($obj)
  $bytes = [Text.Encoding]::UTF8.GetBytes($json)
  $ws.SendAsync([ArraySegment[byte]]$bytes, [System.Net.WebSockets.WebSocketMessageType]::Text, $true, [Threading.CancellationToken]::None).Wait()
}
function Recv-Msg() {
  $buf = New-Object byte[] 4194304
  $ms = New-Object IO.MemoryStream
  do {
    $r = $ws.ReceiveAsync([ArraySegment[byte]]$buf, [Threading.CancellationToken]::None).Result
    $ms.Write($buf, 0, $r.Count)
  } while (-not $r.EndOfMessage)
  return [Text.Encoding]::UTF8.GetString($ms.ToArray())
}
function Call-Cdp($method, $params) {
  $script:msgId++
  $id = $script:msgId
  Send-Msg @{ id = $id; method = $method; params = $params }
  while ($true) {
    $raw = Recv-Msg
    $m = $ser.DeserializeObject($raw)
    if ($m.ContainsKey('id') -and $m['id'] -eq $id) { return $m }
  }
}
function Eval-Js($expr, [bool]$await = $false) {
  $m = Call-Cdp 'Runtime.evaluate' @{ expression = $expr; returnByValue = $true; awaitPromise = $await }
  if ($m.ContainsKey('error')) { throw ("cdp error: " + $ser.Serialize($m['error'])) }
  $res = $m['result']
  if ($res.ContainsKey('exceptionDetails')) { throw ("js exception: " + $ser.Serialize($res['exceptionDetails'])) }
  return $res['result']['value']
}
function Wait-Load() {
  for ($i = 0; $i -lt 60; $i++) {
    Start-Sleep -Milliseconds 1000
    $state = Eval-Js 'document.readyState'
    if ($state -eq 'complete') { Start-Sleep -Seconds 3; return }
  }
}
function Safe-Name($url) {
  $u = [Uri]$url
  $n = [IO.Path]::GetFileName($u.AbsolutePath)
  if (-not $n) { $n = 'index' }
  return ($n -replace '[^A-Za-z0-9._-]', '_')
}

if ($CoolDownSec -gt 0) { Start-Sleep -Seconds $CoolDownSec }
[void](Call-Cdp 'Page.enable' @{})
$log = New-Object System.Collections.Generic.List[string]
$log.Add("page`tlink_text`thref`tsaved_as`tbytes`tstatus")

foreach ($url in $Pages) {
  $slug = Safe-Name $url
  $dir = Join-Path $OutRoot $slug
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  [void](Call-Cdp 'Page.navigate' @{ url = $url })
  Wait-Load
  $title = Eval-Js 'document.title'
  $html = Eval-Js 'document.documentElement.outerHTML'
  [IO.File]::WriteAllText((Join-Path $dir 'page.html'), $html, [Text.Encoding]::UTF8)
  Write-Output ("PAGE {0} title='{1}' bytes={2}" -f $slug, $title, $html.Length)
  if ($title -match 'Service unavailable|Access Denied|Forbidden|Azure WAF') {
    Write-Output "BLOCKED-once $url"; Start-Sleep -Seconds 90
    [void](Call-Cdp 'Page.navigate' @{ url = $url }); Wait-Load
    $title = Eval-Js 'document.title'; $html = Eval-Js 'document.documentElement.outerHTML'
    [IO.File]::WriteAllText((Join-Path $dir 'page.html'), $html, [Text.Encoding]::UTF8)
    if ($title -match 'Service unavailable|Access Denied|Forbidden|Azure WAF') { Write-Output "BLOCKED $url"; continue }
  }

  $linksJson = Eval-Js '(()=>{const out=[];for(const a of document.querySelectorAll("a[href]")){const h=a.href;if(/\.(docx|xlsx|xls|pdf|zip)(\?|$)/i.test(h)||/\/media\/document\//i.test(h)){out.push({t:(a.innerText||"").trim().replace(/\s+/g," "),h:h});}}return JSON.stringify(out);})()'
  $links = $ser.DeserializeObject($linksJson)
  $seen = @{}
  foreach ($l in $links) {
    $h = $l['h']
    if ($seen.ContainsKey($h)) { continue }
    $seen[$h] = 1
    $name = Safe-Name $h
    $dest = Join-Path $dir $name
    $status = 'ok'; $bytes = 0
    if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 0)) { $bytes = (Get-Item $dest).Length; $status = 'exists'; $log.Add(("{0}`t{1}`t{2}`t{3}`t{4}`t{5}" -f $slug, $l['t'], $h, $name, $bytes, $status)); continue }
    if ($DelayMs -gt 0) { Start-Sleep -Milliseconds $DelayMs }
    try {
      $js = "(async()=>{const r=await fetch(" + $ser.Serialize($h) + ",{credentials:'include'});if(!r.ok)return 'ERR '+r.status;const b=await r.arrayBuffer();const u=new Uint8Array(b);let s='';for(let i=0;i<u.length;i+=0x8000){s+=String.fromCharCode.apply(null,u.subarray(i,i+0x8000));}return btoa(s);})()"
      $b64 = Eval-Js $js $true
      if ($b64 -like 'ERR *') { $status = $b64 }
      else {
        $data = [Convert]::FromBase64String($b64)
        [IO.File]::WriteAllBytes($dest, $data)
        $bytes = $data.Length
      }
    } catch { $status = 'EXC ' + $_.Exception.Message }
    $log.Add(("{0}`t{1}`t{2}`t{3}`t{4}`t{5}" -f $slug, $l['t'], $h, $name, $bytes, $status))
    Write-Output ("  {0} {1} {2}" -f $status, $bytes, $name)
  }
}
[IO.File]::WriteAllLines((Join-Path $OutRoot 'download-log.tsv'), $log, [Text.Encoding]::UTF8)
if ($CloseBrowser) { try { [void](Call-Cdp 'Browser.close' @{}) } catch {} }
$ws.Dispose()
Write-Output 'DONE'
