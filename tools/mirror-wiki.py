#!/usr/bin/env python3
"""Mirror the GitHub wiki (../FSCc.wiki) into wiki/ so that release archives
carry the pages.

Page content is copied unchanged except that wiki-style relative page links
`[text](Page-Name)` and `[text](Page-Name#anchor)` become
`[text](Page-Name.md)` and `[text](Page-Name.md#anchor)`, so that they
resolve inside the repository. wiki/README.md records the wiki commit that
was mirrored.

Run from the repository root:  python3 tools/mirror-wiki.py
"""
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT.parent / "FSCc.wiki"
DST = ROOT / "wiki"
LINK = re.compile(r"\]\(([^)\s#]+)(#[^)\s]*)?\)")


def main() -> int:
    if not (SRC / ".git").exists():
        print(f"wiki clone not found at {SRC}", file=sys.stderr)
        return 1
    sha = subprocess.check_output(["git", "-C", str(SRC), "rev-parse", "HEAD"], text=True).strip()
    date = subprocess.check_output(["git", "-C", str(SRC), "log", "-1", "--format=%cs"], text=True).strip()
    pages = sorted(p for p in SRC.glob("*.md"))
    names = {p.stem for p in pages}
    DST.mkdir(exist_ok=True)
    for old in DST.glob("*.md"):
        if old.name != "README.md":
            old.unlink()

    def fix(m: re.Match) -> str:
        target, anchor = m.group(1), m.group(2) or ""
        if target in names:
            return f"]({target}.md{anchor})"
        return m.group(0)

    for p in pages:
        (DST / p.name).write_text(LINK.sub(fix, p.read_text(encoding="utf-8")), encoding="utf-8")

    listing = "\n".join(f"- [`{p.name}`]({p.name})" for p in pages)
    (DST / "README.md").write_text(
        f"""# Wiki mirror

This directory mirrors the project's GitHub wiki
(<https://github.com/davidfillmore/FSCc/wiki>) so that repository archives
carry the pages. The {len(pages)} Markdown files come from
`davidfillmore/FSCc.wiki.git` at commit `{sha}`, dated {date}. Page content
is unchanged except that wiki-style relative page links have `.md` appended
so that they resolve here. The wiki is the source of record: edit there,
then re-run `python3 tools/mirror-wiki.py` from the repository root (mirror
refreshed {datetime.date.today().isoformat()}).

[`Home.md`](Home.md) is the entry point.

{listing}
""",
        encoding="utf-8",
    )
    print(f"mirrored {len(pages)} pages from {sha[:7]} ({date}) into {DST.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
