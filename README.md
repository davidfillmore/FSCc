# FSCc

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22410283.svg)](https://doi.org/10.5281/zenodo.22410283)

**The Fillmore–Springer–Cnops construction and inversive geometry.**

The mathematics lives in this repository's
[wiki](https://github.com/davidfillmore/FSCc/wiki), mirrored under
[`wiki/`](wiki/README.md) so that archives carry the pages (the wiki is the
source of record; `python3 tools/mirror-wiki.py` refreshes the mirror). This
repository holds the exact-arithmetic certificates behind it.

**What the wiki covers.** The classical cycle formalism of Schwerdtfeger,
Fillmore–Springer, Cnops, and Kisil connects Möbius geometry with
$\mathrm{SL}_2$-invariant binary forms: cycles are binary quadratics,
zero-radius cycles are points, and the resultant is the power of a point
with respect to a cycle, $\mathrm{tr}(C_Q Z_L)=\mathrm{Res}(L,Q)$. The pages
develop the associated stabilizer tori, elliptic/parabolic/hyperbolic
trichotomy, representation obstructions, and slicing geometry.

**Status.** Every computational claim on the wiki is certified here in exact
arithmetic (SymPy over $\mathbb{Q}$, no floating point).

## Certificates

| Suite | Checks | What it certifies | Transcript |
|---|---|---|---|
| `fscc-verify.py` | 32 | The dictionary identities (block [01]), the stabilizer-torus theorem ([02]), the $n=2$ dead end ([03]), the representation-theoretic obstruction ([05]), and the baseline polynomial-map identities ([00]) | `fscc-verify-output.txt` |
| `slicing-verify.py` | 76 | The $d=3$ slicing trichotomy ([P]), Wlodek's $\mathrm{SL}_2\times\mathbb{A}^1$ model of $\{\mathrm{Res}=1\}$ ([W]), the transverse-slice theorem ([T]), the class lattice and the little groups of the three detectors ([C]), and the dimension and family floors ([F]) | `slicing-verify-output.txt` |

Each suite prints one `PASS`/`FAIL` line per check and exits nonzero on any
failure. The committed transcripts are the runs backing the wiki.

```
python3 -m venv v && v/bin/pip install -r requirements.txt
v/bin/python fscc-verify.py       # ~1 s
v/bin/python slicing-verify.py    # ~10 s
```

## Provenance

The wiki draws on two notes written up by David W. Fillmore in July 2026 and
the accompanying exact-arithmetic certificate suites. The pages and this
repository were prepared on September 5, 2026. Block numbers and check names
are kept so that citations match. The wiki's
[Bibliography and provenance](https://github.com/davidfillmore/FSCc/wiki/Bibliography-and-Provenance)
page records the sources, the surrounding July–September 2026 literature, and
disclosures about concurrent work.

## Citing

Releases are archived on Zenodo. The concept DOI
[10.5281/zenodo.22410283](https://doi.org/10.5281/zenodo.22410283) always
resolves to the latest version; the September 5, 2026 release
`v2026.09.05` is [10.5281/zenodo.22410284](https://doi.org/10.5281/zenodo.22410284).

> D. W. Fillmore, *FSCc*, software and wiki, Zenodo, 2026.
> doi:10.5281/zenodo.22410283

## License

Everything in this repository is dedicated to the public domain under
[CC0 1.0](LICENSE).
