# FSCc: the Fillmore–Springer–Cnops construction and the Jacobian counterexample

> **Status.** Machine-certified. Every computational claim on these pages is
> certified in exact arithmetic by the suites in the
> [FSCc repository](https://github.com/davidfillmore/FSCc) (see
> [Certificates](Certificates.md)). Provenance, sources, and the disclosures owed
> to concurrent work are on
> [Bibliography and provenance](Bibliography-and-Provenance.md).

On July 19–20, 2026, L. Alpöge announced a counterexample to the Jacobian
conjecture in dimension three. Within days T. Tao reconstructed it as the
$`\mathrm{SL}_2(\mathbb{C})`$-equivariant multiplication of binary forms
$`\mathrm{Sym}^1\times\mathrm{Sym}^2\to\mathrm{Sym}^3`$, restricted to the
stratum $`\mathrm{Res}(L,Q)=1`$ and sliced by a differential operator with a
double root. These pages record one observation and what follows from it:

> **The SL₂-invariant core of that construction coincides, exactly
> and not by analogy, with the classical cycle formalism of Schwerdtfeger,
> Fillmore–Springer, Cnops, and Kisil.** Cycles are binary quadratics,
> zero-radius cycles are points, and the resultant *is* the invariant cycle
> product against a zero-radius cycle,
> ```math
> \mathrm{tr}(C_Q\,Z_L)=\mathrm{Res}(L,Q),
> ```
> the classical *power of a point with respect to a circle*. Tao's stratum
> $`\mathrm{Res}=1`$ says the point sits at unit power from the point-pair.

Stated in the idiom of nineteenth-century circle geometry:

> *Take a point and a point-pair on the projective line, with the power of the
> point with respect to the pair equal to one, and form the point-triple; the
> map is three-to-one because a triple splits three ways.*

## Pages

| Page | What it contains |
|---|---|
| [The Fillmore–Springer–Cnops construction](The-Fillmore-Springer-Cnops-Construction.md) | The language: cycles as vectors and as $`2\times2`$ matrices, the Möbius group acting by conjugation, the power of a point, zero-radius cycles, incidence, and Kisil's elliptic/parabolic/hyperbolic (EPH) extension. |
| [The Möbius group and binary forms](The-Mobius-Group-and-Binary-Forms.md) | $`\mathrm{SL}_2`$ on the projective line and on binary forms; weights; the three kinds of one-parameter subgroup; the invariant pairing on $`\mathrm{Sym}^n`$, symmetric for even $`n`$ and alternating for odd $`n`$; why $`\mathrm{Sym}^3`$ lies outside every cycle formalism. |
| [The inversive dictionary](The-Inversive-Dictionary.md) | The counterexample, Tao's reconstruction, and the dictionary theorems: the resultant evaluates the quadratic at the root, $`B(L^2,Q)=-2\,\mathrm{Res}`$, the boxed trace identity, and Möbius equivariance. |
| [The stabilizer torus and the EPH trichotomy](The-Stabilizer-Torus-and-the-EPH-Trichotomy.md) | The $`(1,-1,-2)`$ grading is the split torus fixing the double and simple roots of the slicing operator: a boost. Shaska's weight signatures, the orbit type of the slicing datum, and Kisil's EPH classes coincide, and the counterexample is forced into the hyperbolic class. |
| [The dimension floor](The-Dimension-Floor.md) | Why the mechanism cannot reach the plane: unit power cannot fix the gauge for equal degrees, the $`d=2`$ divisor bookkeeping fails for every hyperplane, two sheets are always symmetric, and no Möbius-equivariant plane counterexample exists. |
| [The slicing trichotomy](The-Slicing-Trichotomy.md) | Three ways to aim the detector: osculating, tangent, transverse to the twisted cubic. Their little groups (Borel, boost, anharmonic $`S_3`$), and the theorem that only the tangent slice is affine space. |
| [Certificates](Certificates.md) | The two exact-arithmetic suites, their check lists, and what they do not cover. |
| [Bibliography and provenance](Bibliography-and-Provenance.md) | Sources, the July–September 2026 literature these pages sit in, disclosures, and the AI statement. |

## Reading order

Readers who know inversive geometry but not the counterexample: start with
[The inversive dictionary](The-Inversive-Dictionary.md). Readers who know the
counterexample but not the cycle formalism: start with
[The Fillmore–Springer–Cnops construction](The-Fillmore-Springer-Cnops-Construction.md).
Everything downstream uses only [The Möbius group and binary forms](The-Mobius-Group-and-Binary-Forms.md).

## Provenance and license

The mathematics on these pages was produced in human-directed sessions with
Claude Fable 5 (Anthropic) on July 26–28, 2026, audited by OpenAI GPT-5.6 Sol
on July 29, 2026, and written up by David W. Fillmore in two notes of July
2026. The pages were prepared on September 5, 2026 by Claude Fable 5.1 under
the same direction. Text and code are dedicated to the
public domain under CC0 1.0, matching the repository's license.
