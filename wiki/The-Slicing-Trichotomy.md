# The slicing trichotomy

> **Status.** Machine-certified: blocks [P], [W], [T], [C] and
> checks F.11–F.15 of `slicing-verify.py` certify every polynomial identity
> and every Euler-characteristic bookkeeping step below (see
> [Certificates](Certificates.md)). The affineness of the tangent slice is
> Tao's and Sawin's [Tao, Speyer], cited. Conventions as on
> [The Möbius group and binary forms](The-Mobius-Group-and-Binary-Forms.md).

## 1. Three ways to aim the detector

One step of Tao's reconstruction is not explained by anything on the earlier
pages: why does the slice $`\{\mathrm{Res}=1,\;D(LQ)=1\}`$ turn out to be
affine space $`\mathbb{C}^3`$, the "miracle"? In his comment thread Tao stated
that no plausible set of *computable invariants* is known that predicts which
invariantly-cut strata of $`\mathrm{Sym}^d`$, or of related equivariant
families, yield slices isomorphic to affine space, and invited experts. Both
defining conditions of the counterexample are invariant cycle-product
normalisations, and the residual grading is the stabilizer torus of the
stratum, so the question is invariant-theory-shaped. This page shows how sharp
it already is at $`d=3`$.

The slicing operator $`D`$ is dual to a binary cubic, a configuration of three
points of its own. Think of it as the *detector*: the slice condition
$`D(LQ)=1`$ is one linear measurement of the produced cubic. Up to
$`\mathrm{SL}_2`$ there are exactly three kinds of detector, by the collision
pattern of its points: all three distinct $`(1,1,1)`$, a double $`(2,1)`$
(Tao's choice), or a triple $`(3)`$. Equivalently, the detector hyperplane
$`H_D\subset\mathbb{P}^3`$ is transverse to, tangent to, or osculating the
twisted cubic $`\Gamma`$ of perfect cubes. Their little groups differ
([stabilizer-torus page, §4](The-Stabilizer-Torus-and-the-EPH-Trichotomy.md)): a
boost for $`(2,1)`$; for $`(1,1,1)`$ only the finite anharmonic group $`S_3`$;
for $`(3)`$ a Borel subgroup.

> **Proposition 7.1** (the $`d=3`$ trichotomy). Let
> $`\pi:\mathbb{P}^1\times\mathbb{P}^2\to\mathbb{P}^3`$ be the multiplication
> map of [Speyer], with ramification divisor $`R=\{\mathrm{Res}=0\}`$ of class
> $`(2,1)`$; for a dual cubic $`D`$ let $`X_D=\{\mathrm{Res}(L,Q)=1,\ D(LQ)=1\}`$
> and $`H_D=\{D=0\}\subset\mathbb{P}^3`$. For every $`D`$ the scaling characters
> of $`(\mathrm{Res},\,D(LQ))`$ are $`(\lambda_1^2\lambda_2,\ \lambda_1\lambda_2)`$,
> a unimodular pair, so each scaling orbit in $`\{\mathrm{Res}\neq0,\,D(LQ)\neq0\}`$
> meets $`X_D`$ exactly once and
> ```math
> X_D\;\cong\;(\mathbb{P}^1\times\mathbb{P}^2)\smallsetminus(R\cup\pi^{-1}H_D).
> ```
> According to the root pattern of $`D`$, equivalently the contact of $`H_D`$
> with the twisted cubic $`\Gamma`$:
>
> **(1)** *Triple root* ($`H_D`$ osculating). Up to equivalence $`D`$ is the
> evaluation $`C\mapsto C(1,0)`$, so $`D(LQ)=L(1,0)\,Q(1,0)=pc`$ and
> $`\pi^{-1}H_D`$ is reducible. On $`X_D=\{\mathrm{Res}=1,\ pc=1\}`$ the
> coordinate $`p`$ is a nonconstant unit, and in fact
> $`X_D\cong\mathbb{G}_m\times\mathbb{A}^2`$; since
> $`\mathcal O(\mathbb{A}^3)^\times=\mathbb{C}^\times`$, $`X_D\not\cong\mathbb{A}^3`$.
>
> **(2)** *Double root* ($`H_D`$ tangent, not osculating). The removed prime
> divisors have classes $`\{(2,1),(1,1)\}`$, a unimodular basis:
> $`\mathrm{Cl}=0`$ and constant units, and $`X_D\cong\mathbb{A}^3`$
> [Tao, Speyer]: the miracle.
>
> **(3)** *Distinct roots* ($`H_D`$ transverse). The removed classes are the
> *same* unimodular pair $`\{(2,1),(1,1)\}`$: again $`\mathrm{Cl}=0`$ and
> constant units, so no divisor-class invariant separates this case from
> case (2). Nevertheless $`X_D\not\cong\mathbb{A}^3`$, by Theorem 7.2 below.

**Proof.** Expanding $`LQ`$ as on the torus page, the orbit representatives
$`\tfrac16\partial_s^3`$, $`\tfrac12\partial_s^2\partial_t`$,
$`\tfrac12(\partial_s^2\partial_t-\partial_s\partial_t^2)`$ extract $`pc`$,
$`pd+qc`$, $`p(d-e)+q(c-d)`$ respectively, and their hyperplane sections of
$`\Gamma`$ at $`\ell=\alpha s+\beta t`$ are $`\alpha^3`$, $`3\alpha^2\beta`$,
$`3\alpha\beta(\alpha-\beta)`$: contact patterns $`(3)`$, $`(2,1)`$,
$`(1,1,1)`$. The character claim is Proposition 6.1 together with the fact
that $`D(LQ)`$ is a linear function of the coefficients of $`LQ`$;
$`\det\begin{pmatrix}2&1\\1&1\end{pmatrix}=1`$ makes the simultaneous
normalisation unique on $`\{\mathrm{Res}\neq0,\ D(LQ)\neq0\}`$, with regular
inverse $`(\mu,\nu)\mapsto(\mu/\nu,\nu^2/\mu)`$. (This is the determinant
$`d-2`$ that vanished at $`d=2`$ in Theorem 6.3: the gauge-fixing impossible
in the plane is uniquely solvable here, for every detector.) A
bidegree-$`(1,1)`$ divisor $`\{\text{bilinear form}=0\}`$ is reducible iff the
form factors as (form in $`L`$)·(form in $`Q`$), i.e. iff its $`2\times3`$
coefficient matrix has rank $`1`$; the ranks here are $`1,2,2`$. In case (1),
$`pc=1`$ makes $`p`$ a unit on $`X_D`$, nonconstant since
$`(p,q,c,d,e)=(1,0,1,0,1)`$ and $`(2,0,\tfrac12,0,\tfrac14)`$ both lie on
$`X_D`$; solving $`\mathrm{Res}=1`$ for $`e=(1+pqd-q^2/p)/p^2`$ exhibits
$`X_D`$ as a graph over $`(p,q,d)\in\mathbb{G}_m\times\mathbb{A}^2`$. In cases
(2)–(3), excision as in Theorem 6.3 gives
$`\mathrm{Cl}=\mathbb{Z}^2/\langle(2,1),(1,1)\rangle=0`$ with trivial relation
lattice, hence constant units. ∎

## 2. The transverse slice is not affine space

> **Theorem 7.2.** Let $`D`$ have three distinct roots (case (3)). Then, with
> $`\chi_c`$ the compactly supported Euler characteristic,
> ```math
> \chi_c(X_D)=0\neq1=\chi_c(\mathbb{A}^3),
> ```
> so $`X_D\not\cong\mathbb{A}^3`$; indeed $`X_D`$ is not contractible, hence not
> an exotic $`\mathbb{A}^3`$ either. The affineness miracle is therefore
> specific to the double-root stratum: among the hyperplane slicings at
> $`d=3`$, exactly the tangent one yields affine space.

**Proof.** Any distinct-roots $`D`$ is carried to $`D_{(1,1,1)}`$ by
$`\mathrm{SL}_2`$ and rescaling (Proposition 7.1), and substitution and
rescaling induce isomorphisms of slices, so take
$`D(LQ)=p(d-e)+q(c-d)`$. By Proposition 7.1,
$`X_D\cong(\mathbb{P}^1\times\mathbb{P}^2)\smallsetminus(R\cup\pi^{-1}H_D)`$;
$`\chi_c`$ is additive over decompositions into locally closed subvarieties
and equals the ordinary $`\chi`$ for complex varieties [PS], so

```math
\chi_c(X_D)=\chi(\mathbb{P}^1\times\mathbb{P}^2)-\chi(R)-\chi(\pi^{-1}H_D)+\chi(R\cap\pi^{-1}H_D)
=6-4-4+\chi(R\cap\pi^{-1}H_D).
```

Indeed $`\chi(R)=4`$: over $`[L]\in\mathbb{P}^1`$ the fibre of $`R`$ is the line
$`\{Q:Q(-q,p)=0\}\subset\mathbb{P}^2`$, the evaluation functional having
coefficient vector $`(q^2,-pq,p^2)`$ on $`(c,d,e)`$, never zero, and a map with
fibres of constant Euler characteristic multiplies; likewise
$`\chi(\pi^{-1}H_D)=4`$, the coefficient matrix of the bilinear form $`D(LQ)`$
having rank $`2`$, hence trivial left kernel, hence line fibres throughout.

The fibre of $`R\cap\pi^{-1}H_D`$ over $`[L]`$ is the intersection of those
two lines: a point where they differ, a line where they coincide, and
coincidence is rank-one degeneration of

```math
\begin{pmatrix}q^2 & -pq & p^2\\ q & p-q & -p\end{pmatrix},
\qquad\text{with }2\times2\text{ minors}\quad q^2(2p-q),\ \ -pq(p+q),\ \ p^2(2q-p).
```

The first and third already have no common zero away from $`p=q=0`$ (their
resultants in either variable are pure monomials), so the two lines are
distinct over *every* $`[L]`$; the unique intersection point is the cross
product of the two rows, a nowhere-vanishing regular map, so
$`[L]\mapsto(L,Q_L)`$ is a section and $`R\cap\pi^{-1}H_D`$ is its image:
$`\chi=\chi(\mathbb{P}^1)=2`$, whence $`\chi_c(X_D)=6-8+2=0`$.

Consistency, tangent case: for $`D_{(2,1)}`$ the second row is $`(q,p,0)`$,
the minors are $`(2pq^2,-p^2q,-p^3)`$, vanishing simultaneously exactly on
$`\{p=0\}`$: one fibre jumps to a line, $`R\cap\pi^{-1}H_D`$ is a section plus
a fibre line, exactly Sawin's description on [Speyer], with $`\chi=1+2=3`$,
giving $`\chi_c=1=\chi_c(\mathbb{A}^3)`$, as it must since that slice *is*
$`\mathbb{A}^3`$. Osculating case: inclusion–exclusion over the reducible
pullback gives $`\chi_c=0=\chi(\mathbb{G}_m\times\mathbb{A}^2)`$, matching
case (1). ∎

In cycle terms: the tangent detector's special alignment with the curve of
zero-radius cubes produces the fibre jump, Sawin's extra line, and that $`+1`$
is exactly what restores the affine-space value; the transverse detector never
aligns. The invariant that decides is not the heavy machinery one might
anticipate but the Euler characteristic.

> **Remark 7.3 (a second route).** A second, independent proof stratifies the
> $`\mathrm{SL}_2\times\mathbb{A}^1`$ model of the resultant hypersurface:
> $`\{\mathrm{Res}=1\}\cong\mathrm{SL}_2(\mathbb{C})\times\mathbb{A}^1`$ via the
> locally nilpotent derivation $`p^2\partial_c+2pq\,\partial_d+q^2\partial_e`$
> with global slice $`s=ce-d^2/4`$, an observation posted by the commenter
> Wlodek on [Tao] (July 25). Transported there, the tangent and transverse
> conditions become
> ```math
> 2puv+qv^2+3p^2q\,s=1,\qquad -pu^2+2(p-q)uv+qv^2+3pq(p-q)\,s=1:
> ```
> the contact pattern reappears as the factorisation of the $`s`$-coefficient
> (a doubled wall versus three simple walls), and counting strata over the
> walls reproduces $`\chi_c=1`$ and $`0`$ (block [W] certifies the model and
> the transported forms; block [T] the wall computations). Three consequences.
> Tao's remark that the miracle "occurs specifically for the double root" is
> a theorem. No ungraded ($`S_3`$-stabilised) counterexample arises from this
> family, so the graded framework of [Shaska] sees everything the $`d=3`$
> family contains. And an affineness criterion for these slices must carry an
> invariant beyond class groups and units; at $`d=3`$ the Euler characteristic
> suffices, $`\chi_c=1`$ holding exactly on the tangent stratum.

## 3. The higher slices and the family floor

> **Proposition 7.4** (the $`d\ge4`$ slices). For every $`d\ge4`$ and every
> hyperplane datum $`D`$, the group $`\mu_{d-2}=\{(\zeta,\zeta^{-1}):\zeta^{d-2}=1\}`$
> acts freely on $`X_D=\{\mathrm{Res}=1,\,D(LQ)=1\}`$ by
> $`(L,Q)\mapsto(\zeta L,\zeta^{-1}Q)`$, the quotient map
> $`X_D\to U=(\mathbb{P}^1\times\mathbb{P}^{d-1})\smallsetminus(R\cup\pi^{-1}H_D)`$
> is finite étale of degree $`d-2`$, and consequently
> ```math
> \chi_c(X_D)=(d-2)\,\chi_c(U)\in(d-2)\mathbb{Z} ,
> ```
> so $`\chi_c(X_D)\neq1`$ and $`X_D\not\cong\mathbb{A}^d`$. (The excision
> computation on [Speyer] shows $`U\not\cong\mathbb{A}^d`$; this closes the
> remaining gap, since for $`d\ge4`$ the slice is a nontrivial cover of $`U`$
> rather than $`U`$ itself.)

**Proof.** The scaling characters of $`(\mathrm{Res},D(LQ))`$ are
$`(\lambda_1^{d-1}\lambda_2,\lambda_1\lambda_2)`$, with determinant $`d-2`$:
the character map $`\mathbb{G}_m^2\to\mathbb{G}_m^2`$ is an isogeny with kernel
$`\mu_{d-2}`$, which fixes both constraints ($`\mathrm{Res}\mapsto\zeta^{d-2}\mathrm{Res}`$)
and acts freely; each scaling orbit in $`\{\mathrm{Res}\neq0,\,D(LQ)\neq0\}`$
meets $`X_D`$ in exactly $`d-2`$ points. Locally over a trivialisation of the
principal $`\mathbb{G}_m^2`$-bundle $`\{(L,Q):L,Q\neq0\}\to\mathbb{P}^1\times\mathbb{P}^{d-1}`$,
with unit functions $`\alpha=\mathrm{Res}`$ and $`\beta=D(LQ)`$ along a
section, the slice is the Kummer cover $`\lambda_1^{\,d-2}=\beta/\alpha`$:
finite étale of degree $`d-2`$ in characteristic zero. The compactly supported
Euler characteristic multiplies along finite étale surjections of complex
varieties, and $`\chi_c(\mathbb{A}^d)=1\notin(d-2)\mathbb{Z}`$ for $`d\ge4`$.
(Tao's thread, comment of July 22, describes, from explicitly uncertified
chatbot output, the same $`(d-2)`$-fold roots-of-unity multiplicity on a
special fibre; the kernel $`\mu_{d-2}`$ is its rigorous global form.) ∎

> **Proposition 7.5** (the $`|a-b|=1`$ wall). In the family
> $`\mu_{a,b}:\mathrm{Sym}^a\times\mathrm{Sym}^b\to\mathrm{Sym}^{a+b}`$ with
> slices $`X=\{\mathrm{Res}(F,G)=1,\ \langle D,FG\rangle=1\}`$, $`D`$ any nonzero
> functional: if $`a=b`$, the torus $`\mathbb{G}_m`$ acts freely on $`X`$ by
> $`(F,G)\mapsto(\lambda F,\lambda^{-1}G)`$, so $`\chi_c(X)=0`$ and
> $`X\not\cong\mathbb{A}^{2a}`$; if $`|a-b|=m\ge2`$, the group $`\mu_m`$ acts
> freely on $`X`$ with finite étale quotient, so $`\chi_c(X)\in m\mathbb{Z}`$
> and $`X\not\cong\mathbb{A}^{a+b}`$. For $`a\ne b`$, the generic degree of the
> rigidified multiplication map onto its target slice is $`m\binom{a+b}{a}`$;
> the resultant normalisation is unique for a chosen root split only when
> $`m=1`$. Thus only the columns $`\mathrm{Sym}^r\times\mathrm{Sym}^{r+1}`$
> survive.

**Proof.** The scaling characters are $`\mathrm{Res}\mapsto\lambda^b\mu^a\,\mathrm{Res}`$
and $`\langle D,FG\rangle\mapsto\lambda\mu\,\langle D,FG\rangle`$; the
character matrix $`\begin{pmatrix}b&a\\1&1\end{pmatrix}`$ has determinant
$`b-a`$. For $`a=b`$ the product-preserving scaling fixes both constraints and
acts freely; for any algebraic $`\mathbb{G}_m`$-action on a complex variety
$`\chi_c(X)=\chi_c(X^{\mathbb{G}_m})`$, and freeness empties the fixed locus.
This also re-proves Theorem 6.2 in one line. For $`|b-a|=m\ge2`$ the kernel of
the character isogeny is $`\mu_m`$, which fixes both constraints and acts
freely; exactly as in Proposition 7.4 the quotient map is a Kummer cover,
finite étale of degree $`m`$, so $`\chi_c(X)=m\,\chi_c(X/\mu_m)`$, and
$`\chi_c(\mathbb{A}^{a+b})=1\notin m\mathbb{Z}`$. Finally, over a general
squarefree product there are $`\binom{a+b}{a}`$ root splits, and for each
split the equation $`\lambda^{b-a}R_0=1`$ has exactly $`m`$ scalar solutions. ∎

In the gauge language of the [floor page](The-Dimension-Floor.md): the unit-power
condition fixes the gauge uniquely exactly on the adjacent-degree columns, and
those are the only columns in which the slice can be affine space. (The
surviving columns for $`r\ge2`$, and what happens along them, are the subject
of the program's separate note on the tower of multiplication slices, outside
this wiki.)

## 4. Where the question stands

Within the family $`\mathbb{P}^1\times\mathbb{P}^{d-1}`$ the criterion now
reads: the slice is $`\cong\mathbb{A}^d`$ iff the removed classes are a
unimodular basis, units are constant, and $`\chi_c=1`$, with the unimodularity
clause binding at $`d\neq3`$ (Skooi's determinant $`d-2`$ and
Proposition 7.4) and off the adjacent-degree columns (Proposition 7.5), and the
topological clause separating the $`d=3`$ strata. Whether these clauses, with
the excision data, are also *sufficient*, by explicit iterated
$`\mathbb{A}^1`$-bundle structures, is one form of Tao's question.

After these results were written, R. van Dobben de Bruyn gave a complete
geometric characterisation of when the complement of a divisor in a projective
bundle over $`\mathbb{P}^1`$ is affine space, provided each component of the
divisor restricts to a hyperplane in every fibre, and applied it to the
counterexample [vDdB]. The slices of Proposition 7.1 are exactly such
complements. Reading that characterisation in the cycle language of these
pages, where the removed divisors are the incidence relation and the detector
hyperplane, is open; see
[Bibliography and provenance](Bibliography-and-Provenance.md).
