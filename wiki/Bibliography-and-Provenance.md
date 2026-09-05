# Bibliography and provenance

## Provenance and statement on the use of AI

The mathematics on these pages is the product of a human–AI collaboration, and
the division of labour should be stated plainly. The work was carried out in
research sessions on July 26–28, 2026 with Claude Fable 5 (Anthropic)
operating at maximum reasoning depth, under the direction of David W. Fillmore.
Fable 5 conducted the literature reconnaissance and adversarial
source-verification (by Claude Opus 5 agents under its orchestration) and
drove much of the creation of the theorems and proofs, bringing the author
along step by step. On July 29, 2026, OpenAI GPT-5.6 Sol, operating at maximum
reasoning depth as the other member of the project's Fable–Sol collaboration,
conducted an independent mathematical audit of the publication surfaces. That
audit identified the missing factor $`|a-b|`$ in the formerly stated general
fibre count (the resultant normalisation has $`|a-b|`$ scalar solutions for
each root split, while equal degrees retain a full $`\mathbb{G}_m`$);
Theorem 6.4 and Proposition 7.5 were corrected accordingly.

The results were written up by the author in two notes, *The inversive
geometry of the Jacobian-conjecture counterexample, via the Fillmore–Springer
construction, and the dimension floor of its mechanism* (revised July 29, 2026)
and a physics-facing companion, both of July 2026. This wiki, prepared on
September 5, 2026 by Claude Fable 5.1 under the same direction, presents that
material reorganised around the cycle-geometric language: the theorem
statements and proofs are those of the notes, with their numbering kept.
Everything is certified in exact arithmetic ([Certificates](Certificates.md)).

## Attribution

The reconstruction of the counterexample as a sliced multiplication map is
Tao's [Tao]; the projective picture, the iterated-$`\mathbb{A}^1`$-bundle
argument, and the excision computation for $`d\ge4`$ are due to Speyer,
W. Sawin, and the commenters "Skooi" and S. Mondal on [Speyer] (the $`d\ge4`$
computations there are unrefereed and are cited as such); the
$`\mathrm{SL}_2\times\mathbb{A}^1`$ model behind the second proof of
Theorem 7.2 is due to the commenter Wlodek on [Tao] (July 25); the graded
no-go in dimension two is Shaska's [Shaska]; Campbell's theorem is from 1973
[Campbell]; the cycle formalism is due to Schwerdtfeger, Fillmore–Springer,
Cnops, and Kisil [Schwerdtfeger, FS, Cnops, Kisil 2010]. The dictionary
identities, the stabilizer-torus theorem, the parity obstruction as applied
here, the dimension floor, and Theorem 7.2 with Propositions 7.4 and 7.5
appeared to be new when written on July 26–29, 2026, with the caveat that the
surrounding discussion was moving quickly. The disclosures below record what a
sweep on September 5, 2026 found.

## Disclosures

1. **Concurrent independent work on the degree-difference weight.** A chain
   of unrefereed candidate manuscripts published by Evidence Press
   (I. Pitchford, maintainer and publisher; attribution "OpenAI Codex /
   Anthropic models", later "Anonymous") states a "degree-difference
   principle" for the multiplication of binary forms of degrees $`r`$ and $`s`$:
   the Jacobian of the resultant chart carries the factor $`(r-s)\,\mathrm{Res}^2`$,
   so the chart is étale on the coprime locus exactly when the characteristic
   does not divide $`s-r`$ and degenerates for $`r=s`$ [EP1, EP2, EP3]. This is
   the same weight computation as Proposition 6.1 and the gauge-fixing reading
   on [The dimension floor](The-Dimension-Floor.md), in Sylvester and Koszul
   language. Their first release page is dated July 27, 2026 and its Zenodo
   record July 28; the notes behind this wiki were worked out on July 26–28
   and first deposited on July 28. Neither work cites the other; the overlap
   is disclosed here, with the chronology, and no priority is claimed in
   either direction.
2. **The mechanism floor is a floor for one mechanism.** Gallagher's family
   [Gallagher], Speyer's tangent-sweep note [Speyer 2], and Gao's
   generalisation [Gao] produce dimension-three counterexamples of every
   generic fibre degree $`n\ge3`$ by a different construction; the floor on
   [The dimension floor](The-Dimension-Floor.md) concerns the binary-form
   multiplication mechanism and its Möbius-equivariant relatives.
3. **The affineness question.** Van Dobben de Bruyn [vDdB] has since given a
   complete geometric characterisation of affine-space complements of
   fibrewise-hyperplane divisors in projective bundles over $`\mathbb{P}^1`$,
   with an appendix on the counterexample; the slices of Proposition 7.1 are
   such complements. That paper states that no AI was used.
4. **The graded framework.** The classification of graded Keller maps, their
   orbits and fields of definition is Shaska's programme, continued with
   Kistner [Shaska, Kistner–Shaska]; these pages use only his weight-signature
   theorem and his plane no-go. Austermann [Austermann] has since certified,
   in Lean 4 with Gröbner-basis certificates, that the counterexample is
   degree-minimal among $`\mathbb{C}^*`$-equivariant Keller maps with weights
   $`(-1,1,2)`$.
5. **Absence from the literature.** The claim on
   [The inversive dictionary](The-Inversive-Dictionary.md) that the cycle-geometric
   reading appears nowhere rests on full-text searches of both corpora and
   citation-graph enumeration in July 2026, and on a September 5, 2026 sweep
   of arXiv (queries in the vocabulary of inversive, Möbius, Lie-sphere, and
   Clifford geometry, binary forms, resultants, and Sylvester matrices, each
   crossed with the Jacobian conjecture or Keller maps, fifty results per
   query), Zenodo, GitHub, and the Tao and Speyer discussion threads. Not
   checked: MathSciNet and zbMATH, non-English sources, and the full texts of
   most 2026 papers beyond their abstracts.

## References

**The counterexample and its discussion**

- **[Alpöge]** L. Alpöge, announcement of a counterexample to the Jacobian conjecture in dimension 3, X (Twitter), July 19–20, 2026. [x.com/\_\_alpoge\_\_/status/2079028340955197566](https://x.com/__alpoge__/status/2079028340955197566).
- **[Tao]** T. Tao, *A digestion of the Jacobian conjecture counterexample*, blog post and comment thread, July 21, 2026. [terrytao.wordpress.com](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- **[Speyer]** D. Speyer, *The new counterexample to the Jacobian conjecture*, Secret Blogging Seminar, post and comment thread, July 20, 2026. [sbseminar.wordpress.com](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
- **[Speyer 2]** D. Speyer, *Jacobian tangent sweep*, note linked from the July 23, 2026 comment on [Speyer]. [PDF](https://sbseminar.wordpress.com/wp-content/uploads/2026/07/jacobiantangentsweep.pdf)
- **[Gallagher]** A. Gallagher, *An infinite family of counterexamples to the Jacobian Conjecture in dimension three: every generic fiber degree n ≥ 3 occurs*, Zenodo, July 20, 2026. [doi:10.5281/zenodo.21479195](https://doi.org/10.5281/zenodo.21479195)
- **[Shaska]** T. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210 (v1 July 22, v2 July 25, 2026).
- **[Kistner–Shaska]** K. Kistner and T. Shaska, *Orbits and Fields of Definition for Graded Keller Maps*, arXiv:2608.02863 (August 3, 2026).
- **[Jelonek]** Z. Jelonek, *On mappings with Jacobian one*, arXiv:2607.20597 (July 22, 2026).
- **[Migus]** P. Migus, *Generic degrees of real polynomial Keller maps with non-dense image*, arXiv:2607.21572 (v1 July 23, v3 August 27, 2026).
- **[Huq-Kuruvilla]** I. Huq-Kuruvilla, *An Explicit Characteristic-2 Counterexample to the Separable Jacobian Conjecture*, arXiv:2607.20968 (July 23, 2026).
- **[Mondello]** R. Mondello, *A Dimension-Two Counterexample to the Separable Jacobian Conjecture in Characteristic Two*, arXiv:2608.02634 (July 29, 2026).
- **[Meng–Yang]** G. Meng and L. Yang, *A five-variable counterexample to the Hessian conjecture, and the low-dimensional status of the Jacobian and Hessian conjectures*, arXiv:2607.22198 (v1 July 24, v2 July 27, 2026).
- **[Gao]** S. Gao, *Counterexamples to the Jacobian conjecture in dimensions greater than two*, arXiv:2608.00222 (July 31, 2026).
- **[vDdB]** R. van Dobben de Bruyn, *Divisors in projective bundles over the projective line whose complement is affine space*, arXiv:2608.27341 (August 27, 2026).
- **[Austermann]** S. Austermann, *The minimal equivariant counterexample to the Jacobian conjecture*, Zenodo, August 24, 2026. [doi:10.5281/zenodo.22085245](https://doi.org/10.5281/zenodo.22085245)
- **[EP1]** Evidence Press (attribution "OpenAI Codex / Anthropic models"; I. Pitchford, publisher), *Candidate evidence bundle for the degree-difference principle and affine slices of binary-form factorisation spaces*, Zenodo, July 28, 2026 (release page dated July 27). [doi:10.5281/zenodo.21647593](https://doi.org/10.5281/zenodo.21647593)
- **[EP2]** Anonymous (Evidence Press), *The bordered Jacobian of binary-form multiplication: an integral foundation for the degree-difference principle*, Zenodo, August 8, 2026. [doi:10.5281/zenodo.21855302](https://doi.org/10.5281/zenodo.21855302)
- **[EP3]** Anonymous (Evidence Press), *Exact Smith Invariants and Affine Determinant Lines of Binary-Form Factorisation*, Zenodo, August 9, 2026. [doi:10.5281/zenodo.21861347](https://doi.org/10.5281/zenodo.21861347)

**The cycle formalism**

- **[FS]** J. P. Fillmore and A. Springer, *Möbius groups over general fields using Clifford algebras associated with spheres*, Internat. J. Theoret. Phys. **29** (1990), no. 3, 225–246. [doi:10.1007/BF00673627](https://doi.org/10.1007/BF00673627)
- **[Schwerdtfeger]** H. Schwerdtfeger, *Geometry of Complex Numbers*, Dover, New York, 1979 (corrected reprint of the 1962 edition).
- **[Cnops]** J. Cnops, *An Introduction to Dirac Operators on Manifolds*, Progress in Mathematical Physics 24, Birkhäuser, Boston, 2002.
- **[Kisil 2010]** V. V. Kisil, *Erlangen program at large-1: Geometry of invariants*, SIGMA **6** (2010), 076, 45 pp. [doi:10.3842/SIGMA.2010.076](https://doi.org/10.3842/SIGMA.2010.076); arXiv:math/0512416.
- **[Kisil 2007]** V. V. Kisil, *Schwerdtfeger–Fillmore–Springer–Cnops construction implemented in GiNaC*, Adv. Appl. Clifford Algebr. **17** (2007), no. 1, 59–70; arXiv:cs/0512073.
- **[Kisil 2012]** V. V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of* $`\mathrm{SL}_2(\mathbb{R})`$, Imperial College Press, London, 2012.
- **[Kisil 2018]** V. V. Kisil, *An extension of Möbius–Lie geometry with conformal ensembles of cycles and its implementation in a GiNaC library*, Proc. Int. Geom. Center **11** (2018), no. 3, 45–67; arXiv:1512.02960.
- **[Kisil 2019]** V. V. Kisil, *Lectures on Möbius–Lie geometry and its extension*, in: Geometry, Integrability and Quantization **20** (2019), 13–61; arXiv:1811.10499.

**Classical results used**

- **[Campbell]** L. A. Campbell, *A condition for a polynomial map to be invertible*, Math. Ann. **205** (1973), 243–248. [doi:10.1007/BF01349234](https://doi.org/10.1007/BF01349234)
- **[Gutwirth]** A. Gutwirth, *The action of an algebraic torus on the affine plane*, Trans. Amer. Math. Soc. **105** (1962), 407–414.
- **[Moh]** T. T. Moh, *On the Jacobian conjecture and the configurations of roots*, J. Reine Angew. Math. **340** (1983), 140–212.
- **[Borisov]** A. Borisov, *Frameworks for two-dimensional Keller maps*, Electron. J. Combin. **27** (2020), no. 3, #P3.54; arXiv:1901.04073.
- **[BCW]** H. Bass, E. H. Connell, and D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse*, Bull. Amer. Math. Soc. (N.S.) **7** (1982), 287–330.
- **[vdE]** A. van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*, Progress in Mathematics 190, Birkhäuser, Basel, 2000.
- **[Bhargava]** M. Bhargava, *Higher composition laws I: A new view on Gauss composition, and quadratic generalizations*, Ann. of Math. (2) **159** (2004), 217–250.
- **[PS]** C. Peters and J. Steenbrink, *Mixed Hodge Structures*, Ergeb. Math. Grenzgeb. (3) **52**, Springer, Berlin, 2008.

## License

Text and code of this wiki and its repository are dedicated to the public
domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/),
matching the repository's license.
