"""Path resolution for the war.gov UAP mirror toolchain.

These scripts live INSIDE the mirror repo (tools/) so the committed copy is the
copy that actually runs — there is no second copy to drift out of sync. That
drift is exactly what stranded three documents for two weeks in 2026-07/08.

  REPO    the git clone (mirror content lives at its root)
  WORK    scratch dir OUTSIDE the repo: csv, page html, partial downloads.
          Nothing here may ever be committed.
  MIRRORS every release clone that together makes up the corpus. New files are
          written to REPO (the active release); "already mirrored?" checks
          must look at all of them, or a new release repo re-downloads the
          whole history. Clones are siblings named uap-release-* in WORK.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get('UAP_WATCHER_WORK', os.path.dirname(REPO))
STAGE = os.path.join(WORK, 'partials')
MIRRORS = sorted({REPO} | {os.path.join(WORK, d) for d in os.listdir(WORK)
                           if d.startswith('uap-release-')
                           and os.path.isdir(os.path.join(WORK, d, '.git'))})
CSV = os.path.join(WORK, 'uap-data.csv')

os.makedirs(STAGE, exist_ok=True)
