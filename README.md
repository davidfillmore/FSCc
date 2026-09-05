# FSCc

**The Fillmore–Springer–Cnops construction and the inversive geometry of the
July 2026 Jacobian-conjecture counterexample.**

The mathematics lives in this repository's
[wiki](https://github.com/davidfillmore/FSCc/wiki). This repository holds the
exact-arithmetic certificates behind it.

**What the wiki says, in one sentence.** The
$\mathrm{SL}_2$-invariant core of Alpöge's counterexample, as reconstructed by
Tao, *is* the classical cycle formalism of Schwerdtfeger, Fillmore–Springer,
Cnops, and Kisil: cycles are binary quadratics, zero-radius cycles are points,
the resultant is the power of a point with respect to a cycle,
$\mathrm{tr}(C_Q Z_L)=\mathrm{Res}(L,Q)$, the $(1,-1,-2)$ grading is the
stabilizer torus of the slicing operator (a boost, so the counterexample is
forced into the hyperbolic class), the target $\mathrm{Sym}^3$ lies outside
every cycle formalism, and the multiplication mechanism has a hard floor at
dimension three.

**Status.** Every computational claim on the wiki is certified here in exact
arithmetic (SymPy over $\mathbb{Q}$, no floating point). The mathematics has
not undergone independent human review. *Certification is not review.*

## Certificates

| Suite | Checks | What it certifies | Transcript |
|---|---|---|---|
| `fscc-verify.py` | 32 | The dictionary identities (block [01]), the stabilizer-torus theorem ([02]), the $n=2$ dead end ([03]), the representation-theoretic obstruction ([05]), and the baseline facts about the map ([00]) | `fscc-verify-output.txt` |
| `slicing-verify.py` | 76 | The $d=3$ slicing trichotomy ([P]), Wlodek's $\mathrm{SL}_2\times\mathbb{A}^1$ model of $\{\mathrm{Res}=1\}$ ([W]), the transverse-slice theorem ([T]), the class lattice and the little groups of the three detectors ([C]), and the dimension and family floors ([F]) | `slicing-verify-output.txt` |

Each suite prints one `PASS`/`FAIL` line per check and exits nonzero on any
failure. The committed transcripts are the runs backing the wiki.

```
python3 -m venv v && v/bin/pip install -r requirements.txt
v/bin/python fscc-verify.py       # ~1 s
v/bin/python slicing-verify.py    # ~10 s
```

## Provenance

The mathematics was produced in human-directed research sessions with Claude
Fable 5 (Anthropic) on July 26–28, 2026, with an independent adversarial audit
by OpenAI GPT-5.6 Sol on July 29, 2026, under the direction of David W.
Fillmore, and written up in two notes of July 2026. The wiki pages and this
repository were prepared on September 5, 2026 by Claude Fable 5.1 under the
same direction, from those notes and the program's private certificate suites; block numbers and check
names are kept so that citations match. The wiki's
[Bibliography and provenance](https://github.com/davidfillmore/FSCc/wiki/Bibliography-and-Provenance)
page records the sources, the surrounding July–September 2026 literature, and
the disclosures the territory record requires.

## License

Everything in this repository is dedicated to the public domain under
[CC0 1.0](LICENSE).
