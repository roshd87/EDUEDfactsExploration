# Ed-Fi Reference Artifacts

This directory contains immutable, upstream Ed-Fi Data Standard source artifacts used as
mapping evidence. It is not an ODS/API deployment or runtime dependency.

| Artifact set | Role | Status |
|---|---|---|
| [6.1.0](6.1.0/README.md) | Approved Ed-Fi mapping baseline | Use for new mapping work |
| [5.2.0](5.2.0/README.md) | Earlier analysis evidence | Historical only; do not treat as the approved baseline |

Both sets are pinned to an upstream tag and full commit, retain their downloaded tag archive, and
record local SHA-256 checksums in their version index. The pre-existing
`sources/edfi/swagger-canonical.json` is intentionally preserved in place; it is an ODS/API 7.3
metadata capture for Data Standard 5.2.0, not an Ed-Fi 6.1 artifact.

For new mappings, use the 6.1.0 `Models`, `Descriptors`, and `Schemas` source artifacts. The
approved descriptor scope is the standard `ed-fi.org` namespace; local descriptors and future API
binding choices remain outside this reference cache.
