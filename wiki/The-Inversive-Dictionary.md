# The inversive dictionary

> **Status.** Machine-certified: every identity on this page is
> block [01] or [00] of `fscc-verify.py` (see [Certificates](Certificates.md)).
> Conventions are those of [The Möbius group and binary forms](The-Mobius-Group-and-Binary-Forms.md).

## 1. The counterexample and Tao's reconstruction

On July 19–20, 2026, L. Alpöge announced the explicit polynomial map
$`F:\mathbb{C}^3\to\mathbb{C}^3`$,

```math
F(x,y,z)=\bigl(u^3z+y^2u(4+3xy),\; y+3xu^2z+3xy^2(4+3xy),\; 2x-3x^2y-x^3z\bigr),\qquad u=1+xy,\qquad\text{(1)}
```

with $`\det DF\equiv-2`$ and
$`F(0,0,-\tfrac14)=F(1,-\tfrac32,\tfrac{13}{2})=F(-1,\tfrac32,\tfrac{13}{2})`$,
disproving the Jacobian conjecture for all $`n\ge3`$ [Alpöge]; the construction
was credited to the Claude Fable 5 model working in a human-directed session,
and the case $`n=2`$ remains open. Both displayed facts are certified (checks
0.1 and 0.2). Within days, Tao [Tao] identified the structure: $`F`$ is the
multiplication map

```math
\mu:\mathrm{Sym}^1(\mathbb{C}^2)\times\mathrm{Sym}^2(\mathbb{C}^2)\to\mathrm{Sym}^3(\mathbb{C}^2),\qquad (L,Q)\mapsto LQ,\qquad\text{(2)}
```

restricted to $`\{\mathrm{Res}(L,Q)=1\}`$ and sliced by the condition
$`D(LQ)=1`$ for the third-order operator $`D=\tfrac12\partial_s^2\partial_t`$,
whose double-root structure makes the slice polynomially isomorphic to
$`\mathbb{C}^3`$; a generic binary cubic factors three ways as
(linear)×(quadratic), whence the generic $`3`$-to-$`1`$ behaviour. Speyer and
commenters [Speyer] gave the projective picture
$`\mathbb{P}^1\times\mathrm{Sym}^2(\mathbb{P}^1)\to\mathrm{Sym}^3(\mathbb{P}^1)`$
and located the decisive step in a divisor-class (excision/unimodularity)
computation. Tao's coordinates on the slice are $`a=p`$ and, on the slice,
$`y=2qd-pe`$ and $`z=2d^2+ce+6qd^2+3qce-\tfrac92e`$, with forward
parametrisation $`b=q`$, $`b=1+ay`$, $`c=1-\tfrac32ay+a^2z`$ [Tao] (checks 2.6,
2.7).

Both defining conditions of the counterexample are $`\mathrm{SL}_2`$-invariant
normalisations. The theorems below say what they are in the language of
[the Fillmore–Springer–Cnops construction](The-Fillmore-Springer-Cnops-Construction.md).

## 2. Conventions

$`V=\mathbb{C}^2`$ with coordinates $`(s,t)`$; $`L=ps+qt`$,
$`Q=cs^2+dst+et^2`$; $`g\in\mathrm{SL}_2`$ acts by substitution,
$`(f\circ g)(v)=f(gv)`$. $`\mathrm{Res}(L,Q)=p^2e-pqd+q^2c`$,
$`\mathrm{disc}\,Q=d^2-4ce`$, $`B(Q_1,Q_2)=d_1d_2-2c_1e_2-2c_2e_1`$.

*Cycles.* In Kisil's normalisation [Kisil 2010, Def. 3.1] a cycle on the line
is the locus $`ku^2-2lu+m=0`$, encoded (in the elliptic model
$`\breve e_0=i`$, restricting to the invariant hyperplane of self-adjoint
cycles) by the trace-free matrix

```math
C=\begin{pmatrix} l i & m\\ k & -l i\end{pmatrix},\qquad
\langle C_1,C_2\rangle:=\mathrm{tr}(C_1C_2),\qquad \det C=l^2-km,\qquad\text{(4)}
```

on which $`\mathrm{SL}_2(\mathbb{R})`$, and after complexification
$`\mathrm{SL}_2(\mathbb{C})`$, acts by conjugation [Kisil 2010, Prop. 3.3].
Zero-radius cycles are those with $`\det C=0`$; they encode points
equivariantly [Kisil 2010, Def. 3.12, Lemma 3.14]. The identification with
Tao's coefficients is $`(k,l,m)=(c,-d/2,e)`$ for $`Q(u,1)=cu^2+du+e`$, so the
cycle matrix of $`Q`$ is

```math
C_Q=\begin{pmatrix} -\tfrac d2\,i & e\\ c & \tfrac d2\,i\end{pmatrix},
```

and the *unnormalised zero-radius cycle of* $`L=ps+qt`$ is the cycle matrix of
the quadratic $`L^2`$, whose coefficient triple is $`(p^2,2pq,q^2)`$, so
$`(k,l,m)=(p^2,-pq,q^2)`$:

```math
Z_L=\begin{pmatrix} -pq\,i & q^2\\ p^2 & pq\,i\end{pmatrix}.
```

## 3. The dictionary theorems

> **Proposition 3.1 (the resultant evaluates the quadratic at the root).**
> $`(-q{:}p)`$ is the root of $`L`$, and $`\mathrm{Res}(L,Q)=Q(-q,p)`$.

**Proof.** $`L(-q,p)=p(-q)+qp=0`$, and $`Q(-q,p)=cq^2-dpq+ep^2`$, which is
$`\mathrm{Res}`$ term for term. ∎

So $`\mathrm{Res}(L,Q)`$ is the quadratic evaluated at the other object's
point: the homogeneous-coordinate version of the power of the point. Tao's
constraint $`\mathrm{Res}(L,Q)=1`$ is a normalised *non-incidence*: the point
of $`L`$ sits at unit power from the point-pair of $`Q`$, off the cycle, at
calibrated separation.

> **Proposition 3.2 (the polarised form).** $`\mathrm{disc}(L^2)=0`$, and
> $`B(L^2,Q)=-2\,\mathrm{Res}(L,Q)`$.

**Proof.** $`L^2`$ has coefficient triple $`(p^2,2pq,q^2)`$, so
$`\mathrm{disc}(L^2)=4p^2q^2-4p^2q^2=0`$ (perfect squares are the null
vectors), and

```math
B(L^2,Q)=(2pq)d-2p^2e-2q^2c=-2\left(p^2e-pqd+q^2c\right)=-2\,\mathrm{Res}(L,Q). \qquad\blacksquare
```

This is the convention-free heart of the dictionary: the resultant of $`L`$
and $`Q`$ is the invariant inner product of $`Q`$ against the null vector
$`L^2`$. Different sources normalise the cycle pairing with different signs
and factors; Proposition 3.2 is the statement that survives every convention.
The next theorem shows that in Kisil's own matrix convention the constant is
exactly $`1`$.

> **Theorem 3.3** ($`\mathrm{Res}`$ is the power of the point). Let $`C_Q`$ be
> the cycle matrix (4) of $`Q`$ and let $`Z_L`$ be the unnormalised zero-radius
> cycle of $`L`$. Then, in Kisil's convention and with no normalising constant,
> ```math
> \mathrm{tr}(C_{Q_1}C_{Q_2})=-\tfrac12 B(Q_1,Q_2),\qquad
> \det C_Q=\tfrac14\mathrm{disc}\,Q,\qquad \det Z_L=0,
> ```
> ```math
> \boxed{\;\mathrm{tr}(C_Q\,Z_L)=\mathrm{Res}(L,Q)\;}
> ```
> In particular $`\mathrm{tr}(C_QZ_L)=0`$ iff the root of $`L`$ lies on the
> cycle of $`Q`$ (Kisil's incidence relation [Kisil 2010, §4]), and
> $`\mathrm{tr}(C_QZ_L)`$ is the classical power of the point with respect to
> the cycle.

**Proof.** With $`C_j=\begin{pmatrix}l_ji&m_j\\k_j&-l_ji\end{pmatrix}`$, the
diagonal entries of $`C_1C_2`$ are $`-l_1l_2+m_1k_2`$ and $`k_1m_2-l_1l_2`$, so
$`\mathrm{tr}(C_1C_2)=-2l_1l_2+m_1k_2+k_1m_2`$; substituting $`l_j=-d_j/2`$,
$`k_j=c_j`$, $`m_j=e_j`$ gives $`-\tfrac12 d_1d_2+e_1c_2+c_1e_2=-\tfrac12B(Q_1,Q_2)`$.
Next $`\det C_Q=(-\tfrac{d}{2}i)(\tfrac{d}{2}i)-ec=\tfrac{d^2}{4}-ce=\tfrac14\mathrm{disc}\,Q`$,
and $`\det Z_L=\tfrac14\mathrm{disc}(L^2)=0`$ by Proposition 3.2. Finally,
entry by entry,

```math
(C_QZ_L)_{11}=\bigl(-\tfrac{d}{2}i\bigr)(-pq\,i)+e\,p^2=-\tfrac{d}{2}pq+p^2e,\qquad
(C_QZ_L)_{22}=c\,q^2+\bigl(\tfrac{d}{2}i\bigr)(pq\,i)=q^2c-\tfrac{d}{2}pq,
```

whose sum is $`p^2e-pqd+q^2c=\mathrm{Res}(L,Q)`$. (Equivalently:
$`\mathrm{tr}(C_QZ_L)=-\tfrac12B(L^2,Q)=\mathrm{Res}(L,Q)`$ by Proposition 3.2;
the two routes agree.) For incidence, the point matrix
$`Z(u_0)=\begin{pmatrix} iu_0&u_0^2\\1&-iu_0\end{pmatrix}`$ gives, by the same
computation, $`\mathrm{tr}\bigl(C_Q\,Z(u_0)\bigr)=cu_0^2+du_0+e=Q(u_0,1)`$, and
$`Z_L=p^2\,Z(-q/p)`$ homogenises this, consistent with Proposition 3.1. ∎

The three constructions, nineteenth-century circle geometry, the Sylvester
determinant, and the trace pairing of matrices, compute the same number.

> **Proposition 3.4 (equivariance and invariance).** Let
> $`S_Q=\begin{pmatrix}c&d/2\\d/2&e\end{pmatrix}`$ be the Gram matrix of $`Q`$,
> $`J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}`$, and
> $`M_Q:=2JS_Q=\begin{pmatrix}d&2e\\-2c&-d\end{pmatrix}`$. Put
> $`P=\mathrm{diag}(-i,1)`$ and $`\rho(g)=P^{-1}gP`$; explicitly, for
> $`g=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}`$,
> $`\rho(g)=\begin{pmatrix}\alpha&i\beta\\-i\gamma&\delta\end{pmatrix}`$. Then
> $`C_Q=(-i/2)P^{-1}M_QP`$. For $`g\in\mathrm{SL}_2`$: $`Jg^{\mathsf T}J^{-1}=g^{-1}`$,
> hence
> ```math
> M_{Q\circ g}=g^{-1}M_Qg,\qquad
> C_{Q\circ g}=\rho(g)^{-1}C_Q\rho(g),
> ```
> and $`\det M_Q=-\mathrm{disc}\,Q`$ is invariant; consequently $`B`$ and (by
> Proposition 3.2) $`\mathrm{Res}`$ are $`\mathrm{SL}_2`$-invariant:
> $`\mathrm{Res}(L\circ g,Q\circ g)=\mathrm{Res}(L,Q)`$.

**Proof.** For $`g=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}`$
with $`\alpha\delta-\beta\gamma=1`$, a two-line computation gives
$`Jg^{\mathsf T}J^{-1}=\begin{pmatrix}\delta&-\beta\\-\gamma&\alpha\end{pmatrix}=\mathrm{adj}\,g=g^{-1}`$.
Gram matrices transform by congruence, $`S_{Q\circ g}=g^{\mathsf T}S_Qg`$, so
$`M_{Q\circ g}=2Jg^{\mathsf T}S_Qg=(Jg^{\mathsf T}J^{-1})(2JS_Q)g=g^{-1}M_Qg`$.
Direct multiplication gives $`C_Q=(-i/2)P^{-1}M_QP`$, whence
$`C_{Q\circ g}=\rho(g)^{-1}C_Q\rho(g)`$. Hence
$`\mathrm{disc}(Q\circ g)=-\det M_{Q\circ g}=-\det M_Q=\mathrm{disc}\,Q`$;
$`B`$ is invariant as the polarisation of an invariant quadratic; and
$`\mathrm{Res}(L\circ g,Q\circ g)=-\tfrac12B\bigl((L\circ g)^2,Q\circ g\bigr)=-\tfrac12B(L^2\circ g,Q\circ g)=\mathrm{Res}(L,Q)`$. ∎

Thus Kisil's matrices do transform by conjugation, but under the substitution
convention the conjugating matrix is the explicitly embedded $`\rho(g)`$, not
literally $`g`$. Three matrix models are in play ($`M_Q`$; Kisil's $`C_Q`$; the
naive real symmetric $`S_Q`$), presenting one representation with determinants
$`-\mathrm{disc}`$, $`+\tfrac14\mathrm{disc}`$, $`-\tfrac14\mathrm{disc}`$;
$`P`$ changes between the first two, and a model must be fixed before quoting
constants.

## 4. The dictionary, assembled

| Binary forms (Tao, Speyer) | Cycle geometry (Fillmore–Springer, Kisil) | Proved in |
|:---|:---|:---|
| quadratic $`Q\in\mathrm{Sym}^2`$ | cycle $`C_Q`$: trace-free $`2\times2`$, $`\rho`$-conjugation action | Prop. 3.4 |
| point of $`\mathbb{P}^1`$, linear form $`L`$ | zero-radius cycle $`Z_L=C_{L^2}`$ (rank $`1`$, $`\det 0`$) | Prop. 3.2, Thm. 3.3 |
| $`\mathrm{disc}\,Q`$ | $`\det C`$ ($`=`$ radius$`^2`$, model constant) | Thm. 3.3, Prop. 3.4 |
| invariant pairing on $`\mathrm{Sym}^2`$ | cycle product $`\mathrm{tr}(C_1C_2)=-\tfrac12B`$ | Thm. 3.3 |
| "point lies on cycle" | $`\mathrm{tr}(C_QZ(u_0))=Q(u_0)=0`$ | Thm. 3.3 |
| $`\mathrm{Res}(L,Q)`$ | $`\mathrm{tr}(C_QZ_L)=`$ power of the point | Thm. 3.3 |
| Tao's stratum $`\mathrm{Res}=1`$ | unit power: calibrated non-incidence | Thm. 3.3 |
| ramification divisor $`\{\mathrm{Res}=0\}`$ | incidence divisor $`\langle C_Q,Z_L\rangle=0`$ | Props. 3.1, 3.2 |
| $`\mathrm{SL}_2`$-invariance throughout | Möbius covariance of cycles | Prop. 3.4 |

Assembling: *cycle* $`=`$ binary quadratic; *zero-radius cycle* $`=`$ perfect
square $`=`$ point of $`\mathbb{P}^1`$; $`\det=`$ radius² $`=\tfrac14\mathrm{disc}`$;
*cycle product* $`=-\tfrac12\times`$ polarised discriminant; *point-on-cycle
incidence* $`=\{\mathrm{Res}=0\}=`$ the ramification divisor removed in
[Speyer]; and Tao's stratum $`\mathrm{Res}(L,Q)=1`$ is the statement that the point
of $`L`$ sits at unit power from the point-pair of $`Q`$. One may state the
whole counterexample in the idiom of nineteenth-century circle geometry:

> *Take a point and a point-pair on the projective line with the power of the
> point equal to one, and form the point-triple; the map is three-to-one
> because a triple splits three ways.*

The second defining condition, $`D(LQ)=1`$, is a linear measurement of the
produced cubic; it is the subject of the
[stabilizer-torus page](The-Stabilizer-Torus-and-the-EPH-Trichotomy.md) and the
[slicing page](The-Slicing-Trichotomy.md). And the dictionary stops at the cubic:
by Theorem 5.3 on the [Möbius page](The-Mobius-Group-and-Binary-Forms.md), the
target $`\mathrm{Sym}^3`$ carries no invariant symmetric form and lies outside
every cycle formalism.

## 5. On the absence of this translation from the literature

The identification is elementary, but it appears nowhere. As of July 2026,
Kisil's corpus never mentions resultants, $`\mathrm{Sym}^2`$, or
$`\mathfrak{sl}_2`$ in this context (he records $`\mathrm{tr}\,C=0`$ without
the representation-theoretic gloss); conversely no algebraic-geometry or
Jacobian-conjecture source cites the cycle literature: the citation graphs of
[Kisil 2007] and [Kisil 2019] consist entirely of Clifford-analysis and
computer-algebra items, and targeted searches from the Jacobian side return
nothing. Neither [Tao] nor [Speyer] (including comment threads) uses
circle-geometric language. Kisil himself notes that the formalism "ha[s] not
yet propagated back to the most fundamental case of complex numbers"
[Kisil 2019]. A sweep of the aftermath literature on September 5, 2026
(arXiv, Zenodo, GitHub, and the discussion threads; bounds recorded on
[Bibliography and provenance](Bibliography-and-Provenance.md)) found no later
work in this vocabulary. The dictionary is thirty-five years old in the sense
that all its ingredients were in print by 1990; it had not been written down.
