# uap-release-02

Continuation of [ckpxgfnksd-max/uap-release-01](https://github.com/ckpxgfnksd-max/uap-release-01):
a byte-exact mirror of the records published at <https://www.war.gov/UFO/>.

`uap-release-01` holds everything published through the **2026-08-07** tranche
(382 files). Its LFS budget is exhausted, so new records land here, starting with
the **2026-09-18** tranche. The two repos together are the full corpus; nothing is
duplicated between them.

> **Last sync:** 2026-10-04. war.gov lists **450 records**. All 450 are mirrored
> across the two repos (01 + 02). This repo holds **75 files, ~3.5 GB**.

## Contents

| Tranche | Files | What |
|---|---|---|
| 2026-09-18 (mirrored 09-22) | 72 | 56 documents (`DOW-UAP-D102`…, incl. the AAWSAP contract file and the full DIRD technical-report series), 15 videos, 1 audio (`dow-uap-pr160.mp4`, the 1952 Ruppelt presentation) |
| 2026-09-18 (added to war.gov's list later, mirrored 09-27) | 3 | `LLE-UAP-D002`…`D004`, Colorado transcripts accompanying the `lle-uap-pr1…4` videos |

New record-id family in this release: **`LLE-UAP-*`** (Colorado, 2023), named
like the others: `lle-uap-pr<N>.mp4`.

## Naming

| Record | Mirror filename |
|---|---|
| `DOW-UAP-PR0NN` / `LLE-UAP-PR0NN` | `dow-uap-pr<NN>.mp4` / `lle-uap-pr<NN>.mp4` (no leading zeros) |
| `NASA-UAP-D0NN` video | `nasa-uap-d<NN>-<short-slug>.mp4` |
| documents | war.gov medialink URL basename, URL-decoded, verbatim |

## Getting the files

All media is stored with Git LFS.

```bash
git lfs install
git clone https://github.com/ckpxgfnksd-max/uap-release-01.git
git clone https://github.com/ckpxgfnksd-max/uap-release-02.git
```

Use `GIT_LFS_SKIP_SMUDGE=1` to clone pointers only, then `git lfs pull --include="<file>"`
for what you need.

## Mirror toolchain

`tools/` is the watcher that keeps this corpus in sync; it now reads every
`uap-release-*` sibling clone when deciding what is already mirrored. See
[tools/README.md](tools/README.md).

Content is US government work published by war.gov; this repo only mirrors it.
