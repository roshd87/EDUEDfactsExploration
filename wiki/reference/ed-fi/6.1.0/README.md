# Ed-Fi Data Standard 6.1.0

**Role:** approved Ed-Fi mapping baseline.

| Field | Value |
|---|---|
| Upstream repository | `https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard` |
| Immutable tag | `v6.1.0` |
| Immutable commit | `916027186e818c1b33e543c59bc024a9333e00da` |
| Archive source | `https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard/archive/refs/tags/v6.1.0.tar.gz` |
| Local original | `Ed-Fi-Data-Standard-v6.1.0.tar.gz` |
| Archive SHA-256 | `3d18e9597652322ebc33b351ab22db18777fcc51e0672421d656edc3ca019ade` |
| Data handbook | `https://edfidocs.blob.core.windows.net/%24web/handbook/v6.1/index.html` |

The archive is preserved as received. The following original upstream directories are extracted
without transformation for local search:

| Directory | Files | Aggregate SHA-256* |
|---|---:|---|
| `Models/` | 36 | `80df514f8ab16a58dc03ba3eb7f42d39f9b77e92f36d3bfd634e06f44636882a` |
| `Descriptors/` | 266 | `0887079a4fb857fe4d2cf48ba79f3c3329f376193100d78eea867f2b4c909d95` |
| `Schemas/` | 36 | `bc9f9458090bcbd4728114e6fa061dfcfea69d2ec3f32dd9c517b48f9ec87e93` |

\* Aggregate checksum: SHA-256 of lexicographically sorted `sha256sum` output for every regular
file beneath the indicated directory. It detects additions, removals, renames, and content changes
within the local extraction.

The Ed-Fi Alliance identifies v6.1.0 as the current Data Standard v6 release and states that only
the `ed-fi.org` descriptor namespace is part of the standard. Do not use this reference set to
choose an ODS/API version; that physical binding remains deferred.

`Schemas/JSON/` contains upstream simplified schema definitions, not valid OpenAPI specification
files. Consequently, this cache does not supply the formal 6.1 Swagger/OpenAPI binding needed for
automatic resource/property-path validation; selecting and freezing that API binding remains a
separate deferred architecture decision.
