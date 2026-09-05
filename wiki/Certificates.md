# Certificates

Every computational claim on this wiki is certified in exact arithmetic
(SymPy over $`\mathbb{Q}`$, with $`\mathbb{Q}(i)`$ where Kisil's
$`\breve e_0=i`$ appears; no floating point) by two suites in the
[FSCc repository](https://github.com/davidfillmore/FSCc). Each prints one
`PASS`/`FAIL` line per check and exits nonzero on any failure; the committed
`*-output.txt` transcripts are the runs backing these pages. The suites check
identities, ranks, determinants, and bookkeeping; they do not check the prose
arguments that connect them.

```
python3 -m venv v && v/bin/pip install -r requirements.txt   # sympy 1.14.0
v/bin/python fscc-verify.py       # 32 checks, ~1 s
v/bin/python slicing-verify.py    # 76 checks, ~10 s
```

## `fscc-verify.py` (32 checks)

| Block | Checks | Certifies | Page |
|---|---|---|---|
| [01] The dictionary | 1.1–1.6 (16) | $`\mathrm{Res}=p^2e-pqd+q^2c`$; $`\mathrm{Res}=Q(-q,p)`$; $`B(Q,Q)=\mathrm{disc}`$, $`\mathrm{disc}(L^2)=0`$, $`B(L^2,Q)=-2\mathrm{Res}`$; the Kisil trace pairing, $`\det C_Q=\tfrac14\mathrm{disc}`$, $`\det Z=0`$, incidence, $`\mathrm{tr}(C_QZ_L)=\mathrm{Res}`$, $`Z_L=p^2Z(-q/p)`$; $`M_Q=2JS_Q`$, $`Jg^{\mathsf T}J^{-1}=g^{-1}`$, $`M_{Q\circ g}=g^{-1}M_Qg`$, $`\det M_Q=-\mathrm{disc}`$; full $`\mathrm{SL}_2`$-invariance of $`\mathrm{Res}`$ | [The inversive dictionary](The-Inversive-Dictionary.md) |
| [02] The stabilizer torus | 2.1–2.8 (8) | the combined torus preserves $`\mathrm{Res}`$ and $`pd+qc`$; the separate weights of torus and scalings; slice weights $`(2,-2,-4)`$; Tao's parametrisation closes and inverts; $`F(tx,y/t,z/t^2)=(t^{-2}F_1,t^{-1}F_2,tF_3)`$ | [The stabilizer torus](The-Stabilizer-Torus-and-the-EPH-Trichotomy.md) |
| [03] The $`n=2`$ dead end | 3.1–3.3 (3) | $`(1,1)`$: $`\mathrm{Res}`$ is scaling-invariant; $`AD=BC`$ and $`C=B-1`$; $`(1,2)`$: $`\mathrm{Res}\mapsto\lambda_1^2\lambda_2\mathrm{Res}`$ | [The dimension floor](The-Dimension-Floor.md) |
| [05] Representation obstructions | 5.1–5.3 (3) | the pairing on $`\mathrm{Sym}^2`$ is symmetric and on $`\mathrm{Sym}^3`$ alternating; the $`\mathrm{Sym}^3`$ pairing is $`\mathrm{SL}_2`$-invariant; the Clebsch–Gordan dimension count | [The Möbius group and binary forms](The-Mobius-Group-and-Binary-Forms.md) |
| [00] Baseline | 0.1–0.2 (2) | $`\det DF\equiv-2`$; the three-point collision onto $`(-\tfrac14,0,0)`$ | [The inversive dictionary](The-Inversive-Dictionary.md) |

Block numbers follow the program's original phase-1 suite; its block [04]
(a Hessian-conjecture computation) is omitted here as out of scope.

## `slicing-verify.py` (76 checks)

| Block | Checks | Certifies | Page |
|---|---|---|---|
| [P] The $`d=3`$ trichotomy | P1a–P8b (33) | coefficients of $`LQ`$; the three operators extract $`pc`$, $`pd+qc`$, $`p(d-e)+q(c-d)`$; contact patterns $`\alpha^3`$, $`3\alpha^2\beta`$, $`3\alpha\beta(\alpha-\beta)`$; the osculating functional is evaluation; scaling characters and the unimodular matrix $`\begin{pmatrix}2&1\\1&1\end{pmatrix}`$ with integral inverse; bilinear ranks $`1,2,2`$ and irreducibility of the pullbacks and of $`\mathrm{Res}`$; the osculating graph $`e=(1+pqd-q^2/p)/p^2`$ and the nonconstant unit; sample points on the transverse slice; an $`\mathrm{SL}_2`$ lift of the anharmonic swap | [The slicing trichotomy](The-Slicing-Trichotomy.md) |
| [W] Wlodek's model | W.1–W.11 (11) | the derivation $`p^2\partial_c+2pq\partial_d+q^2\partial_e`$ kills $`\mathrm{Res}`$ and is locally nilpotent; its invariants $`u,v`$ and slice $`s`$; $`au-bv=\mathrm{Res}`$; reconstruction and round-trip identities; the transported tangent and transverse conditions; their $`s`$-coefficients factor as $`3a^2b`$ versus $`3ab(a-b)`$ | [The slicing trichotomy](The-Slicing-Trichotomy.md), Remark 7.3 |
| [T] The transverse slice | T.1–T.9 (9) | the wall restrictions in the model; the transverse minors $`q^2(2p-q),-pq(p+q),p^2(2q-p)`$ with pure-monomial resultants (no fibre jump); the tangent minors with common zero locus exactly $`\{p=0\}`$ (one jump); $`R`$ is a $`\mathbb{P}^1`$-fibration; $`\chi_c=0`$ (transverse) and $`1`$ (tangent) by both routes; the osculating consistency point; the verdict | [The slicing trichotomy](The-Slicing-Trichotomy.md), Theorem 7.2 |
| [C] Class lattice and little groups | C.1–C.7 (7) | Smith form of the removed classes; two anharmonic substitutions; the stabilizers of $`s^3`$ (Borel) and $`s^2t`$ (torus) by generic substitution; the Weyl element does not stabilise; $`S_1\times S_2`$ is not normal in $`S_3`$, the trivial subgroup is normal in $`S_2`$ | [The stabilizer torus](The-Stabilizer-Torus-and-the-EPH-Trichotomy.md), [The dimension floor](The-Dimension-Floor.md) |
| [F] The floors | F.1–F.15 (15) | $`\mathrm{Res}(\lambda_1F,\lambda_2G)=\lambda_1^b\lambda_2^a\mathrm{Res}`$ for seven bidegrees from Sylvester matrices; $`\mathrm{disc}(L_1L_2)=\mathrm{Res}^2`$; the $`(1,1)`$ gauge failure; the invariants and the quadric $`\mathcal V`$, its smoothness, the smoothness of its closure and the rank of the boundary conic; the descended map and $`\mathrm{disc}=1`$; $`\mathrm{disc}\circ\pi=\delta^2`$, the tangent pencil, the tangency, the difference-of-roots unit; the character determinants $`d-2`$ and $`b-a`$; $`\mu_{d-2}`$ fixes both constraints; $`\lambda^m=1`$ has $`m`$ solutions; the generic degree $`3`$ at $`(1,2)`$ and the divisibility obstruction | [The dimension floor](The-Dimension-Floor.md), [The slicing trichotomy](The-Slicing-Trichotomy.md) |

Blocks [P], [W], [T] and checks C.1–C.2 are ported from the program's private
phase-2 preflight suite (July 27, 2026) and phase-2 blocks [06], [09-pre] and
[09] (July 28–29, 2026; check T.6 carries the repair from the July 29
cross-model review). Checks C.3–C.7 and block [F] were written for this
repository on September 5, 2026.

## What is not certified here

- **Cited theorems.** Campbell's theorem, Shaska's theorems, Gutwirth's
  linearisation, the additivity and multiplicativity of $`\chi_c`$ [PS], and the
  excision sequence are used as published results.
- **The affineness of the tangent slice** (Proposition 7.1(2)) is Tao's
  explicit coordinates and Sawin's bundle argument [Tao, Speyer]; the suites
  certify the parametrisation identities (checks 2.6–2.7) and the divisor
  bookkeeping, not the isomorphism itself.
- **The higher excision data** on $`\mathbb{P}^1\times\mathbb{P}^{d-1}`$, $`d\ge4`$,
  (the ranks of the detector forms and the unimodularity failure for each
  $`d`$) are certified in the program's private phase-2 block [07], which is not
  reproduced here; Proposition 7.4 is certified here at the level of the
  character isogeny, the kernel $`\mu_{d-2}`$, and the divisibility arithmetic.
- **The higher columns** $`\mathrm{Sym}^r\times\mathrm{Sym}^{r+1}`$, $`r\ge2`$,
  and their point counts are outside this wiki.
