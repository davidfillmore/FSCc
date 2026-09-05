# The dimension floor

> **Status.** Machine-certified: block [03] of `fscc-verify.py`
> and block [F] and checks C.6–C.7 of `slicing-verify.py` certify every
> identity below (see [Certificates](Certificates.md)). Campbell's theorem,
> Shaska's theorem, and Gutwirth's theorem are cited, not reproved.
> Conventions as on [The Möbius group and binary forms](The-Mobius-Group-and-Binary-Forms.md).

The mechanism at $`n=3`$ multiplies $`\mathrm{Sym}^1\times\mathrm{Sym}^2\to\mathrm{Sym}^3`$.
Why not run $`\mathrm{Sym}^1\times\mathrm{Sym}^1\to\mathrm{Sym}^2`$ and disprove
the *plane* Jacobian conjecture too? This page proves that everything fails at
once at $`n=2`$, by three independent walls, and that no Möbius-organised
variant can reach the plane either:

1. the $`(1,1)`$ case degenerates *completely*: the unit-power condition
   $`\mathrm{Res}=1`$ fails to fix the gauge, and the normalised construction
   collapses to an isomorphism of quadrics with no multivaluedness at all
   (Theorem 6.2);
2. the divisor bookkeeping fails for *every* choice of removed hyperplane at
   $`d=2`$, leaving either a divisor class or a nonconstant unit
   (Theorem 6.3);
3. generic fibre degree $`2`$ is impossible for Keller maps in *every*
   dimension: two sheets force a $`\mathbb{Z}/2`$ deck symmetry, and Galois
   Keller maps are invertible by Campbell's theorem (Theorem 6.4);
4. any $`\mathrm{SL}_2`$-, Möbius-, or cycle-equivariant plane construction is
   closed by Shaska's theorem (Theorem 6.5).

Throughout, $`L_1=p_1s+q_1t`$ and $`L_2=p_2s+q_2t`$.

## 1. The gauge condition and its $`(1,1)`$ failure

> **Proposition 6.1 (scaling weight; the (1,1) degeneracy).** For forms of
> degrees $`(a,b)`$,
> ```math
> \mathrm{Res}(\lambda_1L,\lambda_2Q)=\lambda_1^b\lambda_2^a\,\mathrm{Res}(L,Q);
> ```
> the product-preserving scaling $`(\lambda L,\lambda^{-1}Q)`$ therefore acts
> on $`\mathrm{Res}`$ with weight $`\lambda^{b-a}`$, trivially iff $`a=b`$.
> Moreover for two linear forms $`\mathrm{disc}(L_1L_2)=\mathrm{Res}(L_1,L_2)^2`$.

**Proof.** The Sylvester matrix has $`b`$ rows of $`L`$-coefficients and $`a`$
rows of $`Q`$-coefficients; scaling rows scales the determinant accordingly.
For the identity: $`L_1L_2`$ has coefficients $`(p_1p_2,\;p_1q_2+q_1p_2,\;q_1q_2)`$
and $`(p_1q_2+q_1p_2)^2-4p_1p_2q_1q_2=(p_1q_2-q_1p_2)^2`$, while
$`\mathrm{Res}(L_1,L_2)=p_1q_2-q_1p_2`$. ∎

In cycle language: the scaling $`(\lambda L,\lambda^{-1}Q)`$ is a gauge
transformation, since it does not move the product $`LQ`$, and the unit-power
condition $`\mathrm{Res}=1`$ is a gauge-fixing slice. For $`a\neq b`$ the
gauge transformation moves the power with weight $`b-a`$, so the slice meets a
generic orbit in $`|b-a|`$ points, uniquely only in the adjacent-degree case
$`|a-b|=1`$. For $`a=b`$ the would-be gauge-fixing function is itself gauge
invariant: *the condition cannot fix the gauge at all*. Every failure in
Theorem 6.2 flows from this. (The same weight computation, in Sylvester and
Koszul language, was published concurrently and independently by another
group as a "degree-difference principle"; see the disclosure on
[Bibliography and provenance](Bibliography-and-Provenance.md).)

## 2. The $`(1,1)`$ case degenerates completely

> **Theorem 6.2.** Consider $`\mu:\mathrm{Sym}^1\times\mathrm{Sym}^1\to\mathrm{Sym}^2`$.
>
> **(1)** $`\{\mathrm{Res}=1\}\subset\mathbb{A}^4`$ is the variety
> $`\mathrm{SL}_2(\mathbb{C})`$ (the coefficient matrix
> $`\begin{pmatrix}p_1&q_1\\p_2&q_2\end{pmatrix}`$ has determinant
> $`\mathrm{Res}`$), and the product-preserving scaling is the free left action
> of the diagonal torus $`T`$, with closed orbits.
>
> **(2)** The invariant ring of that action is $`\mathbb{C}[A,B,C,D]/(AD-BC)`$
> for $`A=p_1p_2,B=p_1q_2,C=q_1p_2,D=q_1q_2`$, and on $`\mathrm{Res}=1`$ (i.e.
> $`C=B-1`$) the quotient is the smooth affine quadric
> $`\mathcal V=\{AD=B(B-1)\}\subset\mathbb{A}^3`$, with
> $`\mathrm{Cl}(\mathcal V)\cong\mathbb{Z}\neq0`$; in particular
> $`\mathcal V\not\cong\mathbb{A}^2`$.
>
> **(3)** The descended multiplication map is the restriction of the
> affine-linear isomorphism $`(A,B,D)\mapsto(c,d,e)=(A,2B-1,D)`$, carrying
> $`\mathcal V`$ isomorphically onto $`\{\mathrm{disc}=1\}\subset\mathrm{Sym}^2`$:
> the $`\mathrm{Res}`$-normalised $`(1,1)`$ construction produces no
> multivaluedness at all. The only two-valued object in the family is the
> unnormalised cover $`\{(Q,\rho):\rho^2=\mathrm{disc}\,Q\}\to\{\mathrm{disc}\neq0\}`$,
> $`\rho=\mathrm{Res}(L_1,L_2)`$: the classical square-root double cover, étale
> exactly off the discriminant, with deck transformation the factor swap.

**Proof.** (1) is immediate; freeness and closedness of $`T`$-orbits follow
since a row of an $`\mathrm{SL}_2`$-matrix is nonzero and degenerates in the
limit $`\alpha\to0,\infty`$. (2) A monomial is invariant iff its
$`(p_1,q_1)`$-degree equals its $`(p_2,q_2)`$-degree, and then it factors into
the four displayed quadratics; those are precisely the entries of the outer
product $`(p_1,q_1)^{\mathsf T}(p_2,q_2)`$, whose image closure is the
irreducible determinantal hypersurface $`\{AD-BC=0\}`$ with prime ideal
$`(AD-BC)`$; eliminating $`C=B-1`$ gives $`\mathcal V`$, whose smoothness is a
gradient check: the gradient of $`B^2-B-AD`$ is $`(-D,\,2B-1,\,-A)`$, vanishing
only at $`(0,\tfrac12,0)`$, which is not on $`\mathcal V`$. For the class
group: the projective closure $`\{B^2-BW-AD=0\}\subset\mathbb{P}^3`$ is a smooth
quadric $`\cong\mathbb{P}^1\times\mathbb{P}^1`$, and the boundary
$`\{W=0\}`$-section $`\{B^2=AD\}`$ is a rank-$`3`$, hence irreducible, conic of
class $`(1,1)`$; excision gives $`\mathrm{Cl}(\mathcal V)=\mathbb{Z}^2/\langle(1,1)\rangle\cong\mathbb{Z}`$,
while $`\mathrm{Cl}(\mathbb{A}^2)=0`$. (3) The product's coefficients are
$`(A,\,B+C,\,D)=(A,\,2B-1,\,D)`$ on $`\mathrm{Res}=1`$, and
$`(2B-1)^2-4AD=4(B^2-B-AD)+1=1`$ on $`\mathcal V`$; the map is affine-linear
with inverse $`(c,d,e)\mapsto(c,\tfrac{d+1}2,e)`$. On $`\mathrm{Res}=+1`$
exactly one ordering of each factorisation survives (the swap flips the sign
of $`\mathrm{Res}`$), which is why no multivaluedness remains; without the
normalisation, Proposition 6.1 identifies the two orderings over a squarefree
$`Q`$ with the two square roots of $`\mathrm{disc}\,Q`$. ∎

Part (3) is a familiar object in cycle terms: the eigenvalues of the traceless
matrix model $`M_Q`$ of the cycle are $`\pm\sqrt{\mathrm{disc}\,Q}`$, so
$`\rho=\pm\sqrt{\mathrm{disc}\,Q}`$ is its splitting function, two-valued
around the zero-radius cone. The plane analogue of the counterexample *is*
that double cover and nothing more. This is the precise content of Tao's
remark (comment of July 26 on [Tao]) that in the plane "scaling invariance
prevents normalisation," leaving a punctured domain and the classical
Vitushkin-type example rather than a Keller candidate.

## 3. The $`d=2`$ divisor computation fails for every hyperplane

> **Theorem 6.3.** Let $`\pi:\mathbb{P}^1\times\mathbb{P}^1\to\mathbb{P}^2=\mathrm{Sym}^2(\mathbb{P}^1)`$,
> $`((p_1{:}q_1),(p_2{:}q_2))\mapsto(p_1p_2:p_1q_2+q_1p_2:q_1q_2)`$, with
> ramification divisor the diagonal $`\Delta=\{p_1q_2-q_1p_2=0\}`$ of class
> $`(1,1)`$, and let $`H\subset\mathbb{P}^2`$ be any line. Then
> $`U=(\mathbb{P}^1\times\mathbb{P}^1)\smallsetminus(\Delta\cup\pi^{-1}H)`$ is
> never isomorphic to $`\mathbb{A}^2`$:
>
> **(1)** if $`H`$ is tangent to the branch conic $`\{\mathrm{disc}=0\}`$, then
> $`H=\ell_r`$ (the divisors through a fixed root $`r`$) and $`\pi^{-1}H`$ is
> *reducible*, $`\{x_1=r\}\cup\{x_2=r\}`$; removing the three prime divisors
> leaves $`\mathrm{Cl}(U)=0`$ but $`\mathcal O(U)^\times/\mathbb{C}^\times\cong\mathbb{Z}`$,
> generated by the difference-of-roots unit; since
> $`\mathcal O(\mathbb{A}^2)^\times=\mathbb{C}^\times`$, $`U\not\cong\mathbb{A}^2`$;
>
> **(2)** if $`H`$ is not tangent, $`\pi^{-1}H`$ is irreducible of class
> $`(1,1)`$ and $`\mathrm{Cl}(U)=\mathbb{Z}^2/\langle(1,1)\rangle\cong\mathbb{Z}\neq0=\mathrm{Cl}(\mathbb{A}^2)`$.
>
> In the determinant bookkeeping of the excision computation of [Speyer]
> (comment of "Skooi"), the removed classes are $`\{(1,1),(1,1)\}`$ with
> determinant $`d-2=0`$: the $`d=2`$ needle cannot be threaded.

**Proof.** $`\pi^*\mathcal O(1)=\mathcal O(1,1)`$: the coordinate line
$`\{c=0\}`$ pulls back to $`\{p_1p_2=0\}`$, of class $`(1,0)+(0,1)`$, and all
lines are linearly equivalent. The tangent line to the conic of squares at
$`[L_0^2]`$ is the pencil $`\ell_{r_0}`$ of divisors containing the root
$`r_0`$ of $`L_0`$ (checked at $`r_0=\infty`$: $`\{c=0\}`$ meets $`\{d^2=4ce\}`$
in the double point $`(0{:}0{:}1)`$), and its pullback is
$`\{x_1=r_0\}\cup\{x_2=r_0\}`$, classes $`(1,0)`$ and $`(0,1)`$. Conversely a
reducible pullback contains some $`\{x_1=r\}`$, forcing
$`H\supseteq\pi(\{r\}\times\mathbb{P}^1)=\ell_r`$ and hence $`H=\ell_r`$
tangent. The two exact-sequence computations are then immediate from

```math
1\to\mathbb{C}^\times\to\mathcal O(U)^\times\to\oplus_i\mathbb{Z} D_i\to\mathrm{Cl}(\mathbb{P}^1\times\mathbb{P}^1)\to\mathrm{Cl}(U)\to0:
```

in case (1) the relation lattice $`\ker\bigl(\mathbb{Z}^3\to\mathbb{Z}^2\bigr)`$
for classes $`(1,1),(1,0),(0,1)`$ is generated by $`(1,-1,-1)`$, giving the
unit (for $`r_0=\infty`$ it is $`(p_1q_2-q_1p_2)/(p_1p_2)=q_2/p_2-q_1/p_1`$,
the difference of the two roots); in case (2) the cokernel is
$`\mathbb{Z}^2/\langle(1,1)\rangle`$. Finally
$`\mathrm{disc}\circ\pi=(p_1q_2-q_1p_2)^2`$ (Proposition 6.1) identifies
$`\Delta`$ as the ramification divisor with $`\pi^*(\text{branch conic})=2\Delta`$. ∎

## 4. No two-sheeted Keller maps, in any dimension

Three lemmas and one cited theorem.

> **Lemma 6.4a** (the generic polynomial has monodromy $`S_n`$). Let
> $`k(e_1,\dots,e_n)\subset k(t_1,\dots,t_n)`$ be the inclusion of the field of
> symmetric rational functions into all rational functions of $`n`$ variables
> ($`\mathrm{char}\,k=0`$; $`e_i`$ the elementary symmetric functions). This
> extension is Galois with group $`S_n`$.

**Proof.** $`k(t_1,\dots,t_n)`$ is generated over $`K:=k(e_1,\dots,e_n)`$ by
the roots of $`f(X)=\prod_i(X-t_i)`$, and $`f`$ is separable because the
$`t_i`$ are algebraically independent, hence distinct. A splitting field of a
polynomial with distinct roots is Galois, with $`\mathrm{Gal}\hookrightarrow S_n`$
acting on the roots; conversely every permutation of $`t_1,\dots,t_n`$ is a
field automorphism fixing each $`e_i`$. So $`\mathrm{Gal}=S_n`$. ∎

> **Lemma 6.4b** (degree-$`2`$ extensions are Galois). If $`[E:F]=2`$ and
> $`\mathrm{char}\,F=0`$, then $`E/F`$ is Galois.

**Proof.** $`E=F(\theta)`$ for any $`\theta\in E\smallsetminus F`$, with
minimal polynomial $`X^2+\beta X+\gamma`$ over $`F`$; the other root is
$`-\beta-\theta\in E`$. So $`E`$ is a splitting field of a separable quadratic,
hence Galois, with group $`\mathbb{Z}/2`$ swapping the roots. ∎

> **Lemma 6.4c (Young subgroups are almost never normal).** For $`n=a+b\ge3`$
> with $`a,b\ge1`$, the subgroup $`S_a\times S_b\le S_n`$ is not normal. For
> $`(a,b)=(1,1)`$ it is.

**Proof.** If $`n\ge3`$ then $`\max(a,b)\ge2`$, so the subgroup contains a
transposition. A normal subgroup containing a transposition contains all
transpositions, which generate $`S_n`$; so normality would force
$`S_a\times S_b=S_n`$, contradicting its index $`\binom na\ge n\ge3`$. ∎ (Checks
C.6 and C.7 verify the two cases $`n=3`$ and $`n=2`$ by direct conjugation.)

> **Theorem 6.4** (no Keller map has generic fibre degree two; the floor is
> $`n=3`$).
>
> **(1)** If a Keller map $`F:\mathbb{C}^n\to\mathbb{C}^n`$ has generic fibre
> of cardinality $`2`$, then it is invertible, so no such map exists. *(Uses
> Campbell's theorem [Campbell]: a Keller map inducing a Galois extension of
> function fields is invertible.)*
>
> **(2)** For the slice $`X_{a,b,D}:=\{\mathrm{Res}(F,G)=1=D(FG)\}`$ of
> $`\mu_{a,b}:\mathrm{Sym}^a\times\mathrm{Sym}^b\to\mathrm{Sym}^{a+b}`$, put
> $`n=a+b`$ and $`m=|b-a|`$. If $`a=b`$, product-preserving scaling leaves a
> residual $`\mathbb{G}_m`$ in every nonempty fibre, so the construction does
> not define a dominant generically finite map onto the full target slice. If
> $`m\gt0`$, the generic fibre has $`m\binom{n}{a}`$ elements. Only when $`m=1`$
> is the resultant normalisation unique for each root split; in that
> adjacent-degree case the source field is the fixed field of $`S_a\times S_b`$
> in the generic $`S_n`$ splitting field, and the extension is non-Galois for
> $`n\ge3`$. Hence $`n=2`$ forces the equal-degree degeneration, and the
> minimum the mechanism attains is $`n=3`$, $`(a,b)\in\{(1,2),(2,1)\}`$, fibre
> degree $`3`$: the Alpöge case.

**Proof.** (1) In characteristic $`0`$ the generic fibre cardinality equals the
field degree; a degree-$`2`$ extension is Galois by Lemma 6.4b; Campbell's
theorem applies, and invertible maps have generic fibre $`1`$.

(2) Fix a general squarefree $`C`$ on the target slice and one split of its
roots into an $`a`$-set and a $`b`$-set. Choose $`F_0G_0=C`$ realising that
split. Every factorisation with the same split is $`(F,G)=(\lambda F_0,\lambda^{-1}G_0)`$,
and, with $`R_0=\mathrm{Res}(F_0,G_0)\neq0`$,
$`\mathrm{Res}(\lambda F_0,\lambda^{-1}G_0)=\lambda^{\,b-a}R_0`$ by
Proposition 6.1. If $`a=b`$, the normalisation is independent of $`\lambda`$,
leaving a $`\mathbb{G}_m`$-fibre whenever it is met. If $`a\neq b`$, the
equation $`\lambda^{b-a}R_0=1`$ has exactly $`m=|b-a|`$ distinct solutions over
$`\mathbb{C}`$. Since there are $`\binom na`$ root splits, the generic degree is
$`m\binom na`$.

When $`m=1`$, $`\lambda`$ is determined rationally and introduces no Kummer
radical. Adjoining all roots of the generic $`C`$ gives an $`S_n`$-extension
(Lemma 6.4a), and choosing its $`a`$-set gives the fixed field of
$`S_a\times S_b`$, non-normal for $`n\ge3`$ (Lemma 6.4c). When $`m\gt1`$, the
normalisation introduces a Kummer extension, so the preceding description is
not asserted for the Galois closure of the full rigidified map. Finally, for
$`a\neq b`$ the two slice equations cut the $`(n+2)`$-dimensional source to
dimension $`n`$, matching the target slice. The only positive pair at $`n=2`$
is equal-degree; at $`n=3`$ both pairs are adjacent and have degree $`3`$. ∎

The moral for sheet-counting: *two sheets are always globally symmetric* (a
square root has its $`\pm`$), and global sheet symmetry is fatal for a Keller
counterexample by Campbell. Three sheets can be asymmetric: the counterexample
has monodromy $`S_3`$ but no globally defined deck transformation, because
$`S_1\times S_2`$ is not normal in $`S_3`$. The counterexample lives at the
smallest sheet number where perfect exchange symmetry can fail.

## 5. The equivariant route is closed in the plane

> **Theorem 6.5 (equivariant closure in the plane).** A nontrivial algebraic
> action of $`\mathrm{SL}_2(\mathbb{C})`$ on a variety restricts nontrivially to
> its diagonal torus. Combined with Shaska's theorem [Shaska, Thm. 3.4], that
> every Keller map of $`\mathbb{C}^2`$ equivariant for algebraic
> $`\mathbb{G}_m`$-actions on source and target, with the source action
> nontrivial, is an automorphism (via linearisability of $`\mathbb{G}_m`$-actions
> on $`\mathbb{A}^2`$ [Gutwirth]), no plane Keller counterexample admits a
> nontrivial $`\mathrm{SL}_2`$-, Möbius-, or cycle-geometric equivariance.
> Together with Theorems 6.2–6.4, every route by which the cycle formalism
> could organise a planar counterexample is closed.

**Proof.** The kernel of the action is a closed normal subgroup of
$`\mathrm{SL}_2(\mathbb{C})`$, hence $`\{1\}`$, $`\{\pm I\}`$, or
$`\mathrm{SL}_2(\mathbb{C})`$; if the torus acted trivially the kernel would be
infinite, forcing the whole action trivial. The rest is the cited theorem and
the results above; Möbius and cycle-geometric structures contain one-parameter
subgroups, so they are covered. ∎

> **Remark 6.6 (scope).** Nothing here bears on the truth of the
> two-dimensional Jacobian conjecture itself; the results delimit *this
> mechanism and its equivariant relatives*. Constraints on a hypothetical
> planar counterexample from other directions include Moh's degree bound [Moh]
> and its successors, Borisov's frameworks [Borisov], and, after the
> counterexample, the reductions of Meng–Yang [Meng–Yang]
> ($`\mathrm{HC}_4\Rightarrow\mathrm{JC}_2`$, with the Hessian conjecture false
> for $`n\ge5`$ and open exactly at $`n=4`$), Jelonek's genericity theorem
> [Jelonek], and Migus's classification of real generic degrees [Migus] (even,
> $`\ge4`$; degree $`2`$ excluded exactly as in Theorem 6.4). In positive
> characteristic the separable analogue is refuted by Huq-Kuruvilla in
> dimension three [Huq-Kuruvilla] and by Mondello in dimension two [Mondello],
> both in characteristic two. The floor proved here is a floor *for the
> binary-form multiplication mechanism*: other mechanisms produce dimension-three
> counterexamples of every generic fibre degree $`n\ge3`$ (Gallagher's family
> [Gallagher], explained by Speyer's tangent-sweep note [Speyer 2] and
> generalised by Gao [Gao]), none of degree two, as part (1) requires.
