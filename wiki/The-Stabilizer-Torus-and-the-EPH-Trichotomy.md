# The stabilizer torus and the EPH trichotomy

> **Status.** Machine-certified: Theorem 4.1 is block [02] of
> `fscc-verify.py` (checks 2.1–2.8); the little groups of §4 are checks C.2–C.7
> of `slicing-verify.py` (see [Certificates](Certificates.md)). Conventions as on
> [The inversive dictionary](The-Inversive-Dictionary.md).

## 1. Where does the $`(1,-1,-2)`$ grading come from?

Immediately after the announcement, Speyer observed [Speyer] that the map (1)
is *weighted-homogeneous*: for $`\deg(x,y,z)=(-1,1,2)`$ every monomial
balances. Shaska [Shaska] organised equivariant Keller maps by such weight
signatures and called (1) the minimal *hyperbolic* case, weights $`(1,-1,-2)`$.

This grading is not an extra structure. The construction starts from a large
symmetry group, $`\mathrm{SL}_2`$ acting by substitution on $`(L,Q)`$ times
two independent rescalings $`(L,Q)\mapsto(\lambda_1L,\lambda_2Q)`$, and then
imposes two conditions, $`\mathrm{Res}(L,Q)=1`$ and $`D(LQ)=1`$. Each condition
breaks part of the symmetry. What survives is exactly a one-parameter group;
its charges on the slice coordinates are $`(2,-2,-4)\propto(1,-1,-2)`$; and its
$`\mathrm{SL}_2`$-part is precisely the *stabilizer of the double-root
configuration* of $`D`$, which, having two distinct fixed points on the
projective line, is a Möbius transformation of the hyperbolic kind. In the
language of the [construction page](The-Fillmore-Springer-Cnops-Construction.md),
the residual symmetry is a boost, and its hyperbolic character is forced by the
geometry of the slicing operator.

## 2. The theorem

The symmetry group of $`\mu(L,Q)=LQ`$ is $`\mathrm{SL}_2\times\mathbb{G}_m\times\mathbb{G}_m`$:
substitution $`(L,Q)\mapsto(L\circ g,Q\circ g)`$, under which
$`LQ\mapsto(LQ)\circ g`$, and the scalings, under which
$`LQ\mapsto\lambda_1\lambda_2\,LQ`$. Inside it sits the rank-$`3`$ torus
$`T\times\mathbb{G}_m^2`$ with $`T=\{T_\lambda=\mathrm{diag}(\lambda,\lambda^{-1})\}`$.

> **Theorem 4.1 (the stabilizer torus).** In the torus $`T\times\mathbb{G}_m^2`$,
> the subgroup preserving both constraints $`\{\mathrm{Res}(L,Q)=1\}`$ and
> $`\{D(LQ)=1\}`$, $`D=\tfrac12\partial_s^2\partial_t`$, is exactly the
> one-parameter group
> ```math
> g_\lambda=T_\lambda\circ\bigl(L\mapsto\lambda L,\;Q\mapsto\lambda^{-2}Q\bigr),
> ```
> acting on coefficients by $`(p,q,c,d,e)\mapsto(\lambda^2p,\,q,\,c,\,\lambda^{-2}d,\,\lambda^{-4}e)`$
> and on Tao's slice coordinates by
> ```math
> (a,y,z)\longmapsto(\lambda^{2}a,\;\lambda^{-2}y,\;\lambda^{-4}z),
> ```
> i.e. with weights $`(2,-2,-4)\propto(1,-1,-2)`$. Moreover the stabilizer of
> $`D`$ up to scalar in $`\mathrm{SL}_2`$ is exactly $`T`$ (and $`-I`$ already
> lies in $`T`$).

**Proof.** *Step 1: the second constraint is a coefficient.* Expanding,
$`LQ=pc\,s^3+(pd+qc)\,s^2t+(pe+qd)\,st^2+qe\,t^3`$, and applying
$`D=\tfrac12\partial_s^2\partial_t`$ monomial by monomial ($`D(s^3)=0`$,
$`D(s^2t)=1`$, $`D(st^2)=0`$, $`D(t^3)=0`$) gives $`D(LQ)=pd+qc`$: the
constraint reads off the $`s^2t`$-coefficient of the product.

*Step 2: how the torus acts.* Under $`T_\lambda`$: $`(p,q)\mapsto(\lambda p,\lambda^{-1}q)`$
and $`(c,d,e)\mapsto(\lambda^2c,\,d,\,\lambda^{-2}e)`$, so each monomial of
$`\mathrm{Res}`$ is fixed ($`p^2e`$, $`pqd`$, $`q^2c`$ all have total weight
$`0`$), while $`pd+qc\mapsto\lambda(pd+qc)`$: weight $`+1`$. Under the scalings
$`(\lambda_1,\lambda_2)`$, the Sylvester matrix has two $`L`$-rows and one
$`Q`$-row, so $`\mathrm{Res}\mapsto\lambda_1^2\lambda_2\,\mathrm{Res}`$, and
$`D(LQ)`$, a coefficient of $`LQ\mapsto\lambda_1\lambda_2LQ`$, has weight
$`\lambda_1\lambda_2`$.

*Step 3: solve the character equations.* An element $`(T_\lambda,\lambda_1,\lambda_2)`$
preserves both level sets iff $`\lambda_1^2\lambda_2=1`$ and
$`\lambda\lambda_1\lambda_2=1`$, i.e. $`\lambda_2=\lambda_1^{-2}`$ and
$`\lambda=\lambda_1`$: the family $`g_\lambda`$. Two independent character
equations on a rank-$`3`$ torus leave a rank-$`1`$ subtorus. Composing the
actions gives the coefficient action displayed; on both constraints,
$`p^2e-pqd+q^2c\mapsto\lambda^4p^2\lambda^{-4}e-\lambda^2p\,q\,\lambda^{-2}d+q^2c`$
and $`pd+qc\mapsto\lambda^2p\,\lambda^{-2}d+qc`$.

*Step 4: slice weights.* $`a=p\mapsto\lambda^2a`$. Every term of $`y=2qd-pe`$
has weight $`\lambda^{-2}`$ (e.g. $`pe\mapsto\lambda^2p\cdot\lambda^{-4}e`$),
and every term of $`z=2d^2+ce+6qd^2+3qce-\tfrac92e`$ has weight
$`\lambda^{-4}`$; the forward parametrisation $`b=1+ay`$,
$`c=1-\tfrac32ay+a^2z`$ is manifestly weight-consistent ($`b=q`$ and $`c`$
invariant).

*Step 5:* the stabilizer of $`D`$ is the torus. Identify $`D`$, up to its
constant, with the dual binary cubic $`s^2t`$, i.e. with the root divisor
$`2\cdot[0]+1\cdot[\infty]`$ on $`\mathbb{P}^1`$: a double root and a simple
root at two distinct points. An element $`g\in\mathrm{SL}_2`$ with
$`g\cdot(s^2t)=\mu\,s^2t`$ preserves this divisor, hence permutes its points
respecting multiplicities; since the multiplicities differ, $`g`$ fixes each of
the two points. A Möbius transformation fixing both $`0`$ and $`\infty`$ is
diagonal; conversely $`T_\lambda\cdot(s^2t)=\lambda\,s^2t`$. The Weyl element
swaps the two roots and sends $`s^2t\mapsto st^2`$: it does not stabilise; the
stabilizer is the torus, not its normaliser (checks C.4, C.5).

*Consistency with the explicit map.* Under $`(x,y,z)\mapsto(tx,y/t,z/t^2)`$ one
finds $`u=1+xy`$ invariant and
$`F(tx,y/t,z/t^2)=(t^{-2}F_1,t^{-1}F_2,tF_3)`$ (check 2.8): source weights
$`(1,-1,-2)`$, matching the theorem's $`(2,-2,-4)`$ under $`t=\lambda^2`$, the
$`\mathrm{SL}_2\to\mathrm{PGL}_2`$ double cover; $`-I`$ ($`\lambda=-1`$) acts
trivially on the grading, and the integral generator of the weight ray halves
on descent. ∎

## 3. The EPH unification

> **Corollary 4.2.** The grading of the counterexample is the split torus fixing
> the double root and the simple root of $`D`$. Consequently three
> classifications coincide for this mechanism: Shaska's weight signature
> (hyperbolic: $`0`$ strictly between the weights) $`=`$ the $`\mathrm{SL}_2`$-orbit
> type of the slicing operator (double root $`\ne`$ simple root $`\Rightarrow`$
> split stabilizer, weights of both signs) $`=`$ Kisil's EPH class (hyperbolic:
> subgroup $`A`$, real point-pair). Since the affineness miracle occurs on the
> double-root stratum [Tao, Speyer], the counterexample is *forced* to be
> hyperbolically graded: an all-positive (elliptic) grading, which Shaska proves
> impossible for counterexamples in any dimension [Shaska, Thm. 3.1], could
> never have carried it.

This is Wigner's little-group logic. The one-parameter subgroups of
$`\mathrm{SL}_2(\mathbb{R})`$ come in three conjugacy classes, in Lorentz
language rotations (elliptic, fixed points a conjugate pair), null rotations
(parabolic, one fixed point), and boosts (hyperbolic, two distinct real fixed
points), and Kisil's elliptic, parabolic, and hyperbolic geometries are built on
exactly these [Kisil 2010, Kisil 2012]. A configuration with a double root and
a distinct simple root has two distinguished points; its little group fixes
both; a Möbius map fixing two distinct points is a boost about the axis through
them; and a boost's weights come in opposite-sign pairs, the hyperbolic
signature. The counterexample could not have carried a rotation-like
(definite-sign) grading, because its slicing datum has the wrong kind of
degeneracy. The corollary interprets the classifications *for this mechanism*;
Shaska's theorems stand independently, by his own proofs, and no cycle-space
identity is used in the derivation: it belongs to the common
binary-form/$`\mathrm{SL}_2`$ backbone, with inversive geometry contributing
the parallel vocabulary.

![The elliptic, parabolic, hyperbolic trichotomy](https://raw.githubusercontent.com/wiki/davidfillmore/FSCc/images/eph-trichotomy.svg)

*Figure 2. The three kinds of one-parameter subgroup of SL₂(ℝ) on the upper half-plane, as the three classical pencils of circles: the circles about an interior point (elliptic, a rotation), the horocycles at one boundary point (parabolic), and the arcs through two boundary points (hyperbolic, a boost). The stabilizer torus of the slicing datum fixes its double root and its simple root, so the counterexample's grading is of the third kind.*

## 4. The little groups of the three detectors

The slicing operator $`D`$ is dual to a binary cubic, a configuration of three
points of its own, and up to $`\mathrm{SL}_2`$ there are exactly three kinds:
a triple point, a double and a simple point, or three distinct points. Their
stabilizers up to scalar are, respectively (checks C.2–C.7):

| Root pattern of $`D`$ | Representative | Stabilizer up to scalar | Kind |
|---|---|---|---|
| $`(3)`$ | $`s^3`$ | $`\{\beta=0\}`$, a Borel subgroup | contains a parabolic |
| $`(2,1)`$ | $`s^2t`$ | $`\{\beta=\gamma=0\}=T`$ | hyperbolic (boost) |
| $`(1,1,1)`$ | $`st(s-t)`$ | finite: the anharmonic group $`S_3\subset\mathrm{PGL}_2`$ permuting $`\{0,1,\infty\}`$ | no one-parameter subgroup |

For $`s^3`$, substitution by a generic $`g`$ gives $`(\alpha s+\beta t)^3`$,
a multiple of $`s^3`$ iff $`\beta=0`$; for $`s^2t`$ it gives
$`(\alpha s+\beta t)^2(\gamma s+\delta t)`$, a multiple of $`s^2t`$ iff
$`\beta=\gamma=0`$; for $`W=st(s-t)`$ the substitutions $`(s,t)\mapsto(t,s)`$
and $`(s,t)\mapsto(s,s-t)`$ give $`-W`$ and $`+W`$, two of the six anharmonic
substitutions (projectively; the swap lifts to $`\begin{pmatrix}0&i\\i&0\end{pmatrix}\in\mathrm{SL}_2`$, check P8b). These three little groups are the second half of the
[slicing trichotomy](The-Slicing-Trichotomy.md): the tangent detector is the only
one whose stabilizer is a full torus, and it is the only one whose slice is
affine space.
