# The Möbius group and binary forms

> **Status.** Background plus one theorem. The identities of §4 and §5 are
> certified in block [05] of `fscc-verify.py`; the Sylvester and discriminant
> conventions of §3 in block [01] (see [Certificates](Certificates.md)).

Everything on this wiki rests on one representation-theoretic backbone: the
group $`\mathrm{SL}_2`$, acting on the projective line by Möbius
transformations and on binary forms by substitution. This page fixes the
conventions and proves the one fact that bounds the reach of the cycle
formalism: the binary cubic carries no invariant symmetric form.

## 1. The Möbius group on the projective line

$`\mathrm{SL}_2(\mathbb{C})`$ acts on $`\mathbb{P}^1`$ by Möbius
transformations $`\zeta\mapsto(\alpha\zeta+\beta)/(\gamma\zeta+\delta)`$; the
kernel is $`\{\pm I\}`$, and the quotient $`\mathrm{PGL}_2(\mathbb{C})`$ is the
full Möbius group of the Riemann sphere. Over the reals,
$`\mathrm{SL}_2(\mathbb{R})`$ acts on the real projective line and is the group
whose three kinds of one-parameter subgroup organise Kisil's
elliptic/parabolic/hyperbolic geometries
([construction page, §5](The-Fillmore-Springer-Cnops-Construction.md)). The
$`\mathrm{SL}_2\to\mathrm{PGL}_2`$ double cover is the same bookkeeping as
$`\mathrm{SU}(2)\to\mathrm{SO}(3)`$: the element $`-I`$ acts trivially on
$`\mathbb{P}^1`$, and integral weights halve on descent. (Over $`\mathbb{C}`$
the group is also the double cover of the proper orthochronous Lorentz group,
acting on the celestial sphere; the physics-facing companion notes use that
reading, and it is not needed here.)

The classification of one-parameter subgroups by fixed points on
$`\mathbb{P}^1`$ is what the stabilizer-torus page turns into a theorem: a
Möbius transformation fixing two distinct points is conjugate into the diagonal
torus $`T=\{\mathrm{diag}(\lambda,\lambda^{-1})\}`$ (hyperbolic, a boost); one
fixing exactly one point is unipotent up to conjugacy (parabolic); one with a
conjugate pair of fixed points is a rotation (elliptic).

## 2. Binary forms

Let $`V=\mathbb{C}^2`$ with coordinates $`(s,t)`$. $`\mathrm{Sym}^n`$ denotes
the binary forms of degree $`n`$, an irreducible $`\mathrm{SL}_2`$-representation
of dimension $`n+1`$; it is self-dual, so $`V`$ and $`V^*`$ are not
distinguished. The group acts by *substitution*,

```math
(f\circ g)(v):=f(gv),\qquad g\in\mathrm{SL}_2 ,
```

and the *weight* of a monomial under the torus $`T_\lambda=\mathrm{diag}(\lambda,\lambda^{-1})`$
is its eigenvalue exponent: $`s\mapsto\lambda s`$, $`t\mapsto\lambda^{-1}t`$
gives $`s^{n-i}t^i\mapsto\lambda^{n-2i}s^{n-i}t^i`$, weight $`n-2i`$.

By the fundamental theorem of algebra every binary form factors into linear
forms, $`f=L_1L_2\cdots L_n`$, uniquely up to scalars and ordering; a nonzero
linear form $`L=ps+qt`$ vanishes at the single point $`(-q{:}p)\in\mathbb{P}^1`$.
So a binary form of degree $`n`$ is an unordered configuration of $`n`$ points
of $`\mathbb{P}^1`$ with multiplicity, together with a scale, and multiplication
of forms is the union of configurations. Three features recur:

- **Perfect powers.** All points coincident, $`f=L^n`$: inside
  $`\mathbb{P}(\mathrm{Sym}^n)=\mathbb{P}^n`$ these form the *rational normal
  curve*, the image of $`\mathbb{P}^1\ni L\mapsto L^n`$; for $`n=3`$ it is the
  *twisted cubic* $`\Gamma\subset\mathbb{P}^3`$, the recurring character of the
  [slicing page](The-Slicing-Trichotomy.md). In cycle language $`L^2`$ is a
  zero-radius cycle.
- **The discriminant** vanishes exactly when two points collide.
- **Multiplication merges configurations**, and its fibres are the ways of
  splitting a configuration apart: the source of the counterexample's
  three-to-one behaviour.

## 3. Conventions used throughout

We write $`L=ps+qt`$ and $`Q=cs^2+dst+et^2`$. The resultant of $`L`$ and $`Q`$
is the $`3\times3`$ Sylvester determinant; expanding along the first row,

```math
\mathrm{Res}(L,Q)=\det\begin{pmatrix}p&q&0\\0&p&q\\c&d&e\end{pmatrix}=p^2e-pqd+q^2c .
```

The discriminant is $`\mathrm{disc}\,Q=d^2-4ce`$, with polarisation
$`B(Q_1,Q_2)=d_1d_2-2c_1e_2-2c_2e_1`$, so $`B(Q,Q)=\mathrm{disc}\,Q`$. For two
linear forms, $`\mathrm{Res}(L_1,L_2)=p_1q_2-q_1p_2`$, the $`1{+}1`$ Sylvester
determinant. For forms of degrees $`a`$ and $`b`$ the Sylvester matrix has $`b`$
rows of coefficients of the first form and $`a`$ rows of the second, which is
all the [dimension-floor page](The-Dimension-Floor.md) needs about it.

## 4. The invariant pairing on $`\mathrm{Sym}^n`$, and its parity

> **Proposition 5.1.** Let $`\omega`$ be the symplectic form on $`V`$ and
> $`\Omega=\omega^{\otimes n}`$ restricted to $`\mathrm{Sym}^n\subset V^{\otimes n}`$.
> In the weight basis $`e_i`$ (the symmetrisation of
> $`x^{\otimes(n-i)}\otimes y^{\otimes i}`$), $`\Omega(e_i,e_j)=0`$ unless
> $`j=n-i`$, and $`\Omega(e_i,e_{n-i})=(-1)^i/\binom{n}{i}`$. Thus $`\Omega`$ is
> a nondegenerate $`\mathrm{SL}_2`$-invariant pairing on $`\mathrm{Sym}^n`$,
> symmetric for $`n`$ even and alternating for $`n`$ odd. In particular
> $`\mathrm{Sym}^2`$ carries the discriminant quadratic form and
> $`\mathrm{Sym}^3`$ carries a symplectic form.

**Proof.** Each tensor slot contributes $`\omega(x,x)=\omega(y,y)=0`$ unless it
pairs $`x`$ against $`y`$; writing $`e_i`$ as the average over the
$`\binom{n}{i}`$ slot-arrangements, the surviving pairs of arrangements are
complementary ($`j=n-i`$), each contributing
$`\omega(x,y)^{\,n-i}\omega(y,x)^i=(-1)^i`$, and there are $`\binom{n}{i}`$ of
them, giving $`(-1)^i\binom{n}{i}/\bigl(\binom{n}{i}\binom{n}{n-i}\bigr)=(-1)^i/\binom{n}{i}`$.
Swapping arguments replaces $`(-1)^i`$ by $`(-1)^{n-i}`$: a global factor
$`(-1)^n`$. Invariance follows from $`\omega(gv,gw)=\det(g)\,\omega(v,w)`$;
nondegeneracy from the anti-diagonal matrix with nonzero entries. ∎

> **Proposition 5.2.** The Clebsch–Gordan decompositions of the tensor square
> of $`\mathrm{Sym}^3`$ are
> ```math
> \mathrm{Sym}^3\otimes\mathrm{Sym}^3=\mathrm{Sym}^6\oplus\mathrm{Sym}^4\oplus\mathrm{Sym}^2\oplus\mathrm{Sym}^0,\quad
> S^2=\mathrm{Sym}^6\oplus\mathrm{Sym}^2,\quad \Lambda^2=\mathrm{Sym}^4\oplus\mathrm{Sym}^0.
> ```
> The trivial representation has multiplicity one and lies in $`\Lambda^2`$.

**Proof.** Weight count. The weights of $`\mathrm{Sym}^3`$ are $`\{3,1,-1,-3\}`$;
the $`16`$ pairwise sums form the multiset
$`\{6,4^2,2^3,0^4,(-2)^3,(-4)^2,-6\}`$, and peeling highest weights gives the
tensor decomposition. The $`10`$ unordered-pair sums give
$`\{6,4,2^2,0^2,(-2)^2,-4,-6\}`$, which peels to $`\mathrm{Sym}^6\oplus\mathrm{Sym}^2`$;
the $`6`$ strict-pair sums give $`\{4,2,0^2,-2,-4\}`$, which peels to
$`\mathrm{Sym}^4\oplus\mathrm{Sym}^0`$. ∎

## 5. Why $`\mathrm{Sym}^3`$ is outside every cycle formalism

> **Theorem 5.3.** $`\mathrm{Sym}^3`$ admits no nonzero $`\mathrm{SL}_2`$-invariant
> symmetric bilinear form. Hence there is no $`\mathrm{SL}_2`$-equivariant linear
> identification of $`\mathrm{Sym}^3`$ with any Fillmore–Springer cycle space
> (which carries the invariant symmetric form $`w\cdot w-w^0w^\infty`$ by
> construction [FS]), in any dimension or signature. Moreover the cycle-*matrix*
> calculus is closed in $`M_2\cong\mathrm{Sym}^2\oplus\mathrm{Sym}^0`$ (matrices
> under conjugation), so Kisil's general invariant machinery
> [Kisil 2010, eq. (4.1)], traces and determinants of noncommutative polynomials
> in cycle matrices, can never produce $`\mathrm{Sym}^3`$ either.

**Proof.** By Proposition 5.2 the space of invariant bilinear forms on
$`\mathrm{Sym}^3`$ is one-dimensional and contained in $`\Lambda^2`$; every
invariant form is a multiple of the alternating form of Proposition 5.1, so
$`(S^2\mathrm{Sym}^3)^{\mathrm{SL}_2}=0`$. An equivariant isomorphism onto a
cycle space would pull back its invariant symmetric form to a nonzero element
of that space. For the closure statement: $`M_2=\mathbb{C}I\oplus\mathfrak{sl}_2`$
under conjugation, with $`\mathfrak{sl}_2\cong\mathrm{Sym}^2`$ (weights
$`2,0,-2`$), and $`M_2`$ is closed under products and sums, so any polynomial
expression in cycle matrices remains in $`\mathrm{Sym}^2\oplus\mathrm{Sym}^0`$
and its trace or determinant is invariant. (The Fillmore–Springer *spinors* do
carry $`\mathrm{Sym}^1`$ [FS]; what no cycle-type formalism contains is the
target $`\mathrm{Sym}^3`$ and the multiplication into it.) ∎

> **Remark 5.4.** The dimensional coincidence with the planar cycle space (both
> $`4`$-dimensional) is representation-theoretically empty: cycle spaces are
> orthogonal geometry, binary cubics are symplectic geometry
> ($`\mathrm{SL}_2\subset\mathrm{Sp}_4`$ via $`\mathrm{Sym}^3`$), and the lowest
> invariant of $`\mathrm{Sym}^3`$ is the *quartic* discriminant. The classical
> parametrisation home of $`\mathrm{Sym}^3`$ is the prehomogeneous pair
> $`(\mathrm{GL}_2,\mathrm{Sym}^3)`$ and the Delone–Faddeev/Bhargava
> correspondence [Bhargava], not Möbius–Lie geometry.

This is the precise sense in which the dictionary of the
[next page](The-Inversive-Dictionary.md) is partial: it is exact on the source
$`\mathrm{Sym}^1\times\mathrm{Sym}^2`$ of the counterexample's multiplication
map and cannot be extended to its target.
