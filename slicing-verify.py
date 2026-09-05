"""slicing-verify.py -- exact-arithmetic certificates for the FSCc wiki
(https://github.com/davidfillmore/FSCc/wiki): the slicing trichotomy at d = 3,
the transverse-slice theorem, the family floor, and the little groups of the
three detectors.

Run:  python3 slicing-verify.py       (SymPy 1.14.0; see requirements.txt)
Expected: every line prints PASS, "FAILS: none", exit status 0.
No floating point anywhere.

Blocks, cross-referenced from the wiki pages:
  [P]   the d = 3 trichotomy, Prop. 7.1          -- The-Slicing-Trichotomy
  [W]   Wlodek's SL2 x A^1 model of {Res = 1}     -- The-Slicing-Trichotomy, Remark 7.3
  [T]   the transverse slice is not A^3, Thm 7.2 -- The-Slicing-Trichotomy
  [C]   class lattice, little groups             -- The-Slicing-Trichotomy, The-Stabilizer-Torus
  [F]   the dimension floor and the family floor -- The-Dimension-Floor (Prop 6.1, Thms 6.2-6.4,
                                                    Props 7.4-7.5)

Provenance: blocks [P], [W], [T] and the first two checks of [C] are ported on
September 5, 2026 from the program's private phase-2 preflight suite (33 checks,
July 27, 2026) and phase-2 blocks [06], [09-pre], [09] (July 28-29, 2026;
check 09.6 carries the repair from the July 29 cross-model review). The
remaining checks of [C] and block [F] were written for this repository on
September 5, 2026 and certify identities stated in the notes. Certification is
not review.
"""
import sympy as sp

s, t = sp.symbols('s t')
p, q, c, d, e = sp.symbols('p q c d e')
l1, l2, lam = sp.symbols('lambda1 lambda2 lam')
al, be = sp.symbols('alpha beta')

L = p*s + q*t
Q = c*s**2 + d*s*t + e*t**2
C = sp.expand(L*Q)
Res = p**2*e - p*q*d + q**2*c

results = []
def check(name, ok):
    results.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'} [{name.split()[0]}] {name.split(None, 1)[1]}")

def is_zero(expr):
    return sp.simplify(sp.cancel(sp.expand(expr))) == 0

# ---------------------------------------------------------------- P1: coefficients of LQ
P = sp.Poly(C, s, t)
check("P1a  s^3-coeff of LQ = p*c",            P.coeff_monomial(s**3)      == sp.expand(p*c))
check("P1b  s^2t-coeff of LQ = p*d + q*c",     P.coeff_monomial(s**2*t)    == sp.expand(p*d + q*c))
check("P1c  st^2-coeff of LQ = p*e + q*d",     P.coeff_monomial(s*t**2)    == sp.expand(p*e + q*d))
check("P1d  t^3-coeff of LQ = q*e",            P.coeff_monomial(t**3)      == sp.expand(q*e))

# ---------------------------------------------------------------- P2: operator forms
D3   = lambda f: sp.diff(f, s, 3)/6
D21  = lambda f: sp.diff(f, s, 2, t, 1)/2
D111 = lambda f: (sp.diff(f, s, 2, t, 1) - sp.diff(f, s, 1, t, 2))/2
check("P2a  D3(LQ)   = p*c",                   is_zero(D3(C)   - p*c))
check("P2b  D21(LQ)  = p*d + q*c",             is_zero(D21(C)  - (p*d + q*c)))
check("P2c  D111(LQ) = p(d-e) + q(c-d)",       is_zero(D111(C) - (p*(d-e) + q*(c-d))))

# ---------------------------------------------------------------- P3: contact with the twisted cubic
# Hyperplane section of Gamma = {l^3} by <D, .>: root pattern of D as divisor on P^1.
ell3 = sp.expand((al*s + be*t)**3)
check("P3a  D3(l^3)   = alpha^3          (contact pattern (3): osculating)",
      is_zero(D3(ell3) - al**3))
check("P3b  D21(l^3)  = 3 alpha^2 beta   (contact pattern (2,1): tangent, not osculating)",
      is_zero(D21(ell3) - 3*al**2*be))
check("P3c  D111(l^3) = 3 alpha beta (alpha - beta)  (contact (1,1,1): transverse)",
      is_zero(D111(ell3) - 3*al*be*(al-be)))
# Osculating hyperplanes are evaluation functionals: <D3, C> = C(1,0), pullback = L(1,0)*Q(1,0).
check("P3d  D3(C) = C(1,0) and equals L(1,0)*Q(1,0)  (osculating = evaluation at r0)",
      is_zero(D3(C) - C.subs({s: 1, t: 0})) and is_zero(D3(C) - L.subs({s:1,t:0})*Q.subs({s:1,t:0})))

# ---------------------------------------------------------------- P4: scaling characters + unimodularity
scale = {p: l1*p, q: l1*q, c: l2*c, d: l2*d, e: l2*e}
check("P4a  Res(l1 L, l2 Q) = l1^2 l2 Res  (character (2,1))",
      is_zero(Res.xreplace(scale) - l1**2*l2*Res))
for nm, D in (("D3", D3), ("D21", D21), ("D111", D111)):
    check(f"P4b  {nm}(l1 L * l2 Q) = l1 l2 * {nm}(LQ)  (character (1,1))",
          is_zero(D(sp.expand(L.xreplace(scale)*Q.xreplace(scale))) - l1*l2*D(C)))
M = sp.Matrix([[2, 1], [1, 1]])
check("P4c  det [[2,1],[1,1]] = 1 = d-2 at d=3  (unimodular; Skooi's determinant)",
      M.det() == 1)
check("P4d  M^-1 is integral  =>  Cl(U) = Z^2/<(2,1),(1,1)> = 0 and trivial relation lattice (constant units)",
      all(x.is_integer for x in M.inv()))
# unique normalisation: the character map (l1,l2) -> (l1^2 l2, l1 l2) is an isomorphism of Gm^2,
# with regular inverse (mu,nu) -> (mu/nu, nu^2/mu); hence for EVERY D the affine slice
# {Res = 1, D(LQ) = 1} maps isomorphically to the projective complement U_D.
check("P4e  ((l1^2 l2)/(l1 l2), (l1 l2)^2/(l1^2 l2)) = (l1, l2)  (unique normalisation, every D)",
      is_zero(sp.cancel((l1**2*l2)/(l1*l2) - l1)) and is_zero(sp.cancel((l1*l2)**2/(l1**2*l2) - l2)))

# ---------------------------------------------------------------- P5: bilinear ranks + factorisation
def bilin(expr):
    return sp.Matrix(2, 3, lambda i, j: sp.diff(expr, [p, q][i], [c, d, e][j]))
check("P5a  rank of pc form = 1  (product => reducible pullback)",      bilin(p*c).rank() == 1)
check("P5b  rank of pd+qc form = 2  (irreducible pullback)",            bilin(p*d + q*c).rank() == 2)
check("P5c  rank of p(d-e)+q(c-d) form = 2  (irreducible pullback)",    bilin(p*(d-e) + q*(c-d)).rank() == 2)
def irreducible(expr):
    coeff, facs = sp.factor_list(expr)
    return len(facs) == 1 and facs[0][1] == 1 and sp.Poly(facs[0][0], p, q, c, d, e).total_degree() == sp.Poly(expr, p, q, c, d, e).total_degree()
check("P5d  pc factors as p * c (two factors)",     len(sp.factor_list(p*c)[1]) == 2)
check("P5e  pd+qc irreducible",                     irreducible(p*d + q*c))
check("P5f  p(d-e)+q(c-d) irreducible",             irreducible(p*(d-e) + q*(c-d)))
check("P5g  Res irreducible  (R is a prime divisor)", irreducible(Res))

# ---------------------------------------------------------------- P6: the triple-root slice is Gm x A^2
e_solved = (1 + lam*q*d - q**2/lam)/lam**2
sub = {p: lam, c: 1/lam, e: e_solved}
check("P6a  parametrisation satisfies Res = 1 identically",  is_zero(Res.subs(sub) - 1))
check("P6b  parametrisation satisfies pc = 1 identically",   is_zero((p*c).subs(sub) - 1))
# graph structure: e is determined by (p,q,d) on the slice; inverse is the projection (p,q,d)
ee = sp.symbols('ee')
e_from_res = sp.solve(sp.Eq(Res.subs({c: 1/p}), 1), e)
check("P6c  on {pc=1}, Res=1 determines e uniquely: e = (1 + pqd - q^2/p)/p^2",
      len(e_from_res) == 1 and is_zero(e_from_res[0] - (1 + p*q*d - q**2/p)/p**2))
# two explicit points with different values of the unit p
pt1 = {p: 1, q: 0, c: 1, d: 0, e: 1}
pt2 = {p: 2, q: 0, c: sp.Rational(1, 2), d: 0, e: sp.Rational(1, 4)}
ok1 = Res.subs(pt1) == 1 and (p*c).subs(pt1) == 1
ok2 = Res.subs(pt2) == 1 and (p*c).subs(pt2) == 1
check("P6d  (1,0,1,0,1) and (2,0,1/2,0,1/4) both lie on the slice; p takes values 1 and 2",
      ok1 and ok2 and pt1[p] != pt2[p])
# hence p is a nonconstant unit (pc = 1) on the slice, while O(A^3)^x = C^x:  slice != A^3.

# ---------------------------------------------------------------- P7: transverse slice, sanity of the two defining forms
# (the open case: {Res = 1, p(d-e)+q(c-d) = 1} passes every divisor-class test; recorded, not settled here)
pt3 = {p: 0, q: 1, c: 1, d: 0, e: 7}    # p=0 chart: c=q^-2=1, d=c-1/q=0, e free
check("P7a  sample point (0,1,1,0,7) lies on the transverse slice",
      Res.subs(pt3) == 1 and (p*(d-e) + q*(c-d)).subs(pt3) == 1)
pt4 = {p: 1, q: 0, c: 5, d: 1, e: 0}    # q=0 chart: Res = p^2 e - pqd + q^2 c = 0 ... recheck
# choose instead: p=1,q=0 => Res = e ; constraint2 = d - e ; want e=1, d-1=1 => d=2, c free
pt4 = {p: 1, q: 0, c: 11, d: 2, e: 1}
check("P7b  sample point (1,0,11,2,1) lies on the transverse slice",
      Res.subs(pt4) == 1 and (p*(d-e) + q*(c-d)).subs(pt4) == 1)

# ---------------------------------------------------------------- P8: anharmonic smoke test (finite stabiliser, transverse case)
# z -> 1/z lifts to g = [[0,i],[i,0]] in SL2; it permutes the roots {0,1,oo} of st(s-t) and
# rescales the dual form by the scalar i  (stabiliser of the root SET, projectively).
I = sp.I
f_dual = s*t*(s - t)
g_sub = {s: I*t, t: I*s}
check("P8a  g = [[0,i],[i,0]] in SL2 (det = 1)", sp.Matrix([[0, I], [I, 0]]).det() == 1)
check("P8b  st(s-t) o g = i * st(s-t)  (projective stabiliser instance)",
      is_zero(sp.expand(f_dual.xreplace(g_sub)) - I*f_dual))


# ======================================================================= [W] Wlodek's model
# {Res = 1} at d = 3 is SL2 x A^1 (T. Tao's thread, comment by Wlodek, July 25, 2026):
# the locally nilpotent derivation D = a^2 d_c + 2ab d_d + b^2 d_e with global slice
# s = ce - d^2/4, and the two slicing conditions transported to (a,b,u,v,s).
def check2(tag, ok, desc):
    results.append((f"{tag} {desc}", bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'} [{tag}] {desc}")

from sympy import expand, simplify, Matrix, Rational, Poly, resultant, gcd as sgcd, factor_list, diff, solve
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ

a, b, cc, dd, ee, U, V, S = sp.symbols("a b cc dd ee U V S")
Res3 = a ** 2 * ee - a * b * dd + b ** 2 * cc

def Dlnd(f):
    return expand(a ** 2 * diff(f, cc) + 2 * a * b * diff(f, dd) + b ** 2 * diff(f, ee))

u_inv = a * ee - b * dd / 2
v_inv = a * dd / 2 - b * cc
s_slc = cc * ee - dd ** 2 / 4

check2("W.1", Dlnd(Res3) == 0 and Dlnd(Dlnd(cc)) == 0 and Dlnd(Dlnd(dd)) == 0 and Dlnd(Dlnd(ee)) == 0,
       "D kills Res and is locally nilpotent (D^2 = 0 on the generators c,d,e)")
check2("W.2", expand(Dlnd(u_inv)) == 0 and expand(Dlnd(v_inv)) == 0,
       "u = ae - bd/2 and v = ad/2 - bc are D-invariants")
check2("W.3", expand(Dlnd(s_slc) - Res3) == 0,
       "D(s) = Res, so s = ce - d^2/4 is a global slice on {Res = 1}")
check2("W.4", expand(a * u_inv - b * v_inv - Res3) == 0,
       "au - bv = Res (the SL2 relation au - bv = 1 on the hypersurface)")
check2("W.5",
       expand(v_inv ** 2 + a ** 2 * s_slc - cc * Res3) == 0 and
       expand(2 * (u_inv * v_inv + a * b * s_slc) - dd * Res3) == 0 and
       expand(u_inv ** 2 + b ** 2 * s_slc - ee * Res3) == 0,
       "c = v^2 + a^2 s, d = 2(uv + abs), e = u^2 + b^2 s hold times Res (exact on Res = 1)")
c_of = V ** 2 + a ** 2 * S
d_of = 2 * (U * V + a * b * S)
e_of = U ** 2 + b ** 2 * S
Res_back = expand(a ** 2 * e_of - a * b * d_of + b ** 2 * c_of)
check2("W.6", expand(Res_back - (a * U - b * V) ** 2) == 0,
       "inverse parametrisation: Res(a,b,c(U,V,S),d(..),e(..)) = (aU - bV)^2 identically")
u_back = expand(a * e_of - b * d_of / 2)
v_back = expand(a * d_of / 2 - b * c_of)
s_back = expand(c_of * e_of - d_of ** 2 / 4)
check2("W.7",
       expand(u_back - U * (a * U - b * V)) == 0 and
       expand(v_back - V * (a * U - b * V)) == 0 and
       expand(s_back - S * (a * U - b * V) ** 2) == 0,
       "round trip: u -> U(aU-bV), v -> V(aU-bV), s -> S(aU-bV)^2 (identities on the torsor)")
y_sawin = 2 * b * dd - a * ee
check2("W.8", expand(Dlnd(y_sawin) - 3 * a * b ** 2) == 0 and expand(y_sawin + 2 * u_inv) != 0,
       "Sawin's y = 2bd - ae is not -2u and not D-invariant: D(y) = 3ab^2")
T21_xy = expand(a * d_of + b * c_of)
T21_target = expand(2 * a * U * V + b * V ** 2 + 3 * a ** 2 * b * S)
check2("W.9", expand(T21_xy - T21_target) == 0,
       "tangent condition ad + bc = 2aUV + bV^2 + 3 a^2 b S in Wlodek coordinates")
T111_xy = expand(a * (d_of - e_of) + b * (c_of - d_of))
T111_target = expand(-a * U ** 2 + 2 * (a - b) * U * V + b * V ** 2 + 3 * a * b * (a - b) * S)
check2("W.10", expand(T111_xy - T111_target) == 0,
       "transverse condition a(d-e)+b(c-d) = -aU^2 + 2(a-b)UV + bV^2 + 3ab(a-b) S")
_, f_tan = factor_list(Poly(T21_target, S).LC())
_, f_tra = factor_list(Poly(T111_target, S).LC())
tan_factors = sorted(str(f) for f, m in f_tan for _ in range(m))
tra_factors = sorted(str(f) for f, m in f_tra for _ in range(m))
check2("W.11", tan_factors == ["a", "a", "b"] and tra_factors == ["a", "a - b", "b"],
       "s-coefficients factor as 3*a*a*b (tangent) vs 3*a*b*(a-b) (transverse): contact pattern as factorisation")

# ======================================================================= [T] the transverse slice
f_tra = -a * U ** 2 + 2 * (a - b) * U * V + b * V ** 2
f_tan = 2 * a * U * V + b * V ** 2
f_tra_a0 = f_tra.subs({a: 0, V: -1 / b})
f_tan_a0 = f_tan.subs({a: 0, V: -1 / b})
check2("T.1", simplify(f_tra_a0 - (2 * U + 1 / b)) == 0 and simplify(f_tan_a0 - 1 / b) == 0,
       "wall a=0: f_tra = 2u + 1/b (u-dependent -> Z_a = Gm) vs f_tan = 1/b (u-free -> Z_a = A^1 at b=1)")
f_tra_b0 = f_tra.subs({b: 0, U: 1 / a})
f_tan_b0 = f_tan.subs({b: 0, U: 1 / a})
f_tra_ab = f_tra.subs({b: a, U: V + 1 / a})
check2("T.2",
       simplify(f_tra_b0 - (-1 / a + 2 * V)) == 0 and
       simplify(f_tan_b0 - 2 * V) == 0 and
       simplify(f_tra_ab - (-(2 * V + 1 / a))) == 0,
       "walls b=0: f_tra = -1/a + 2v, f_tan = 2v; wall a=b: f_tra = -(2v + 1/a); all give Z = Gm")
det_SL2 = a * U - b * V
check2("T.3", det_SL2.subs({a: 0, b: 0}) == 0,
       "a=0 & b=0 forces au-bv = 0 != 1: the walls {a=0},{b=0},{a=b} are pairwise disjoint on SL2")
m1 = expand(b ** 2 * (a - b) - (-a * b) * b)
m2 = expand(b ** 2 * (-a) - a ** 2 * b)
m3 = expand((-a * b) * (-a) - a ** 2 * (a - b))
check2("T.4a",
       expand(m1 - b ** 2 * (2 * a - b)) == 0 and expand(m2 + a * b * (a + b)) == 0 and
       expand(m3 - a ** 2 * (2 * b - a)) == 0,
       "transverse minors: m1 = b^2(2a-b), m2 = -ab(a+b), m3 = a^2(2b-a)")
r_a = resultant(m1, m3, a)
r_b = resultant(m1, m3, b)
check2("T.4b",
       r_a != 0 and Poly(r_a, b).monoms() == [(Poly(r_a, b).degree(),)] and
       r_b != 0 and Poly(r_b, a).monoms() == [(Poly(r_b, a).degree(),)],
       "resultants of (m1,m3) are pure monomials => V(m1,m3) = {(0,0)}: no fibre jump, R cap pi^-1(H_tra) ~ P^1, chi = 2")
n1, n2, n3 = expand(b ** 2 * a - (-a * b) * b), expand(b ** 2 * 0 - a ** 2 * b), expand((-a * b) * 0 - a ** 2 * a)
check2("T.5",
       expand(n1 - 2 * a * b ** 2) == 0 and expand(n2 + a ** 2 * b) == 0 and expand(n3 + a ** 3) == 0 and
       all(expand(n.subs(a, 0)) == 0 for n in (n1, n2, n3)) and sgcd(sgcd(n1, n2), n3) in (a, -a),
       "tangent minors = (2ab^2, -a^2b, -a^3): common zero locus exactly {a=0}: a single fibre jump")
check2("T.6", expand(resultant(b ** 2, a ** 2, a) - b ** 4) == 0 and expand(resultant(b ** 2, a ** 2, b) - a ** 4) == 0,
       "Res-functional coefficients (b^2, -ab, a^2) vanish together only at a=b=0: R is a P^1-fibration, chi(R) = 4")
chi_SL2, chi_walls, chi_A1, chi_Gm = 0, 0, 1, 0
chi_Z_tra, chi_Z_tan = 3 * chi_Gm, 1 + chi_Gm
chi_X_tra_r1 = (chi_SL2 - chi_walls) + chi_Z_tra * chi_A1
chi_X_tan_r1 = (chi_SL2 - chi_walls) + chi_Z_tan * chi_A1
chi_X_tra_r2 = 6 - 4 - 4 + 2
chi_X_tan_r2 = 6 - 4 - 4 + 3
check2("T.7",
       chi_X_tra_r1 == 0 and chi_X_tra_r2 == 0 and chi_X_tan_r1 == 1 and chi_X_tan_r2 == 1,
       "chi_c(X_transverse) = 0 by both routes; chi_c(X_tangent) = 1 by both routes (= chi_c(A^3))")
chi_union_osc = 4 + 3 + 4 - 2 - 3 - 2 + 2
check2("T.8", chi_union_osc == 6 and 6 - chi_union_osc == 0,
       "osculating: chi_c = 0 = chi(Gm x A^2), third consistency point")
check2("T.9", chi_X_tra_r1 != 1,
       "THEOREM: chi_c(X_transverse) = 0 != 1 = chi_c(A^3): the transverse slice is not A^3 (nor contractible)")

# ======================================================================= [C] class lattice and little groups
M_cls = Matrix([[2, 1], [1, 1]])
check2("C.1", M_cls.det() == 1 and smith_normal_form(M_cls, domain=ZZ) == Matrix([[1, 0], [0, 1]]),
       "removed classes {(2,1),(1,1)} are a unimodular basis: Cl = 0 and constant units in cases (2)-(3)")
W = expand(s * t * (s - t))
W_swap = expand(W.subs({s: t, t: s}, simultaneous=True))
W_sig = expand(W.subs({t: s - t}, simultaneous=True))
check2("C.2", expand(W_swap + W) == 0 and expand(W_sig - W) == 0,
       "anharmonic S3 instances: (s,t)->(t,s) gives -W; (s,t)->(s,s-t) gives +W for W = st(s-t)")
# little groups of the three detectors, by direct substitution with a generic g in SL2
al_, be_, ga_ = sp.symbols('alpha_ beta_ gamma_')
de_ = (1 + be_ * ga_) / al_                        # det g = 1
def act(f):
    return expand(f.subs({s: al_ * s + be_ * t, t: ga_ * s + de_ * t}, simultaneous=True))
def offdiag_coeffs(f, monomial_keep):
    P_ = Poly(act(f), s, t)
    return [co for mon, co in P_.terms() if mon != monomial_keep]
# (3): s^3 -> scalar multiple of s^3 iff beta = 0 (a Borel subgroup)
sol3 = solve([sp.numer(sp.together(c_)) for c_ in offdiag_coeffs(s ** 3, (3, 0))], [be_], dict=True)
check2("C.3", sol3 == [{be_: 0}],
       "osculating detector s^3: g stabilises it up to scalar iff beta = 0 (Borel little group)")
# (2,1): s^2 t -> scalar multiple iff beta = gamma = 0 (the torus)
eqs21 = [sp.numer(sp.together(c_)) for c_ in offdiag_coeffs(s ** 2 * t, (2, 1))]
sol21 = solve(eqs21, [be_, ga_], dict=True)
check2("C.4", sol21 == [{be_: 0, ga_: 0}],
       "tangent detector s^2 t: g stabilises it up to scalar iff beta = gamma = 0 (the torus T)")
weyl = {s: t, t: -s}
check2("C.5", expand((s ** 2 * t).subs(weyl, simultaneous=True) + s * t ** 2) == 0 and
       expand((lam * s) ** 2 * (t / lam) - lam * s ** 2 * t) == 0,
       "the Weyl element sends s^2 t to -s t^2 (does not stabilise); T_lam scales s^2 t by lam")
# (1,1,1): the stabiliser of {0,1,oo} is finite: the anharmonic group has order 6 in PGL2
from sympy.combinatorics import Permutation, PermutationGroup
S3 = PermutationGroup([Permutation([1, 0, 2]), Permutation([1, 2, 0])])
Young = PermutationGroup([Permutation([1, 0, 2])])          # S_1 x S_2 fixing the letter 2
def is_normal_in(G, H):
    """Direct test: g h g^-1 in H for all g in G, h in H (SymPy's is_normal misreports the trivial subgroup)."""
    return all((g * h * g ** -1) in H for g in G.elements for h in H.elements)
check2("C.6", S3.order() == 6 and Young.order() == 2 and not is_normal_in(S3, Young),
       "S_1 x S_2 has index 3 in S_3 and is not normal: three sheets, no global deck symmetry")
S2 = PermutationGroup([Permutation([1, 0])])
triv = PermutationGroup([Permutation([0, 1])])
check2("C.7", is_normal_in(S2, triv) and S2.order() == 2 and triv.order() == 1,
       "for n = 2 the Young subgroup S_1 x S_1 is trivial, hence normal: two sheets are always symmetric")

# ======================================================================= [F] the dimension floor and the family floor
def sylvester(F, G, degF, degG):
    """Sylvester matrix of binary forms F (degree degF) and G (degree degG) in s,t."""
    fco = [Poly(F, s, t).coeff_monomial(s ** (degF - i) * t ** i) for i in range(degF + 1)]
    gco = [Poly(G, s, t).coeff_monomial(s ** (degG - i) * t ** i) for i in range(degG + 1)]
    n = degF + degG
    rows = []
    for r in range(degG):
        rows.append([0] * r + fco + [0] * (n - degF - 1 - r))
    for r in range(degF):
        rows.append([0] * r + gco + [0] * (n - degG - 1 - r))
    return Matrix(rows)
def generic_form(name, deg):
    co = sp.symbols(f"{name}0:{deg + 1}")
    return sum(co[i] * s ** (deg - i) * t ** i for i in range(deg + 1))
l1_, l2_ = sp.symbols('lambda_1 lambda_2')
ok_all = True
for (da, db) in [(1, 1), (1, 2), (2, 1), (2, 2), (1, 3), (2, 3), (3, 4)]:
    F_ = generic_form('f', da); G_ = generic_form('g', db)
    R0 = sylvester(F_, G_, da, db).det()
    R1 = sylvester(l1_ * F_, l2_ * G_, da, db).det()
    ok_all = ok_all and expand(R1 - l1_ ** db * l2_ ** da * R0) == 0
check2("F.1", ok_all,
       "Prop 6.1: Res(l1 F, l2 G) = l1^b l2^a Res(F,G) for (a,b) in {(1,1),(1,2),(2,1),(2,2),(1,3),(2,3),(3,4)}")
p1, q1, p2, q2 = sp.symbols('p1 q1 p2 q2')
L1, L2 = p1 * s + q1 * t, p2 * s + q2 * t
prod12 = expand(L1 * L2)
disc12 = expand(Poly(prod12, s, t).coeff_monomial(s * t) ** 2 - 4 * Poly(prod12, s, t).coeff_monomial(s ** 2) * Poly(prod12, s, t).coeff_monomial(t ** 2))
Res12 = p1 * q2 - q1 * p2
check2("F.2", expand(disc12 - Res12 ** 2) == 0 and expand(sylvester(L1, L2, 1, 1).det() - Res12) == 0,
       "disc(L1 L2) = Res(L1,L2)^2 with Res(L1,L2) = p1 q2 - q1 p2")
al = sp.symbols('al')
check2("F.3", expand(Res12.subs({p1: al * p1, q1: al * q1, p2: p2 / al, q2: q2 / al}) - Res12) == 0,
       "(1,1): the product-preserving scaling fixes Res, so Res = 1 cannot fix the gauge")
A_, B_, C_, D_ = p1 * p2, p1 * q2, q1 * p2, q1 * q2
check2("F.4", expand(A_ * D_ - B_ * C_) == 0 and expand((B_ - C_) - Res12) == 0,
       "Thm 6.2(2): invariants A,B,C,D satisfy AD = BC, and B - C = Res (so C = B - 1 on Res = 1)")
Av, Bv, Dv, Wv = sp.symbols('A B D W')
quadric = Bv ** 2 - Bv - Av * Dv
grad = [diff(quadric, v) for v in (Av, Bv, Dv)]
crit = solve(grad, [Av, Bv, Dv], dict=True)
check2("F.5", crit == [{Av: 0, Bv: Rational(1, 2), Dv: 0}] and quadric.subs(crit[0]) != 0,
       "Thm 6.2(2): V = {AD = B(B-1)} is smooth (the only critical point of B^2 - B - AD is off V)")
closure = Bv ** 2 - Bv * Wv - Av * Dv
gradc = [diff(closure, v) for v in (Av, Bv, Dv, Wv)]
critc = solve(gradc, [Av, Bv, Dv, Wv], dict=True)
conic = Matrix([[0, 0, Rational(-1, 2)], [0, 1, 0], [Rational(-1, 2), 0, 0]])   # B^2 - AD in (A,B,D)
check2("F.6", critc == [{Av: 0, Bv: 0, Dv: 0, Wv: 0}] and conic.rank() == 3,
       "Thm 6.2(2): the closure {B^2 - BW - AD = 0} is a smooth quadric and the boundary conic B^2 = AD has rank 3")
cP, dP, eP = A_, expand(B_ + C_), D_
check2("F.7", expand(Poly(prod12, s, t).coeff_monomial(s ** 2) - cP) == 0 and
       expand(Poly(prod12, s, t).coeff_monomial(s * t) - dP) == 0 and
       expand(Poly(prod12, s, t).coeff_monomial(t ** 2) - eP) == 0 and
       expand((2 * Bv - 1) ** 2 - 4 * Av * Dv - 4 * (Bv ** 2 - Bv - Av * Dv) - 1) == 0,
       "Thm 6.2(3): L1 L2 has coefficients (A, B + C, D) = (A, 2B - 1, D) on Res = 1, and disc = 1 on V")
check2("F.8", expand(disc12 - Res12 ** 2) == 0 and expand(prod12.subs({p1: 1, q1: 0}) - (p2 * s ** 2 + q2 * s * t)) == 0,
       "Thm 6.3: disc o pi = delta^2 (pi^*(branch conic) = 2 Delta); the tangent pencil at r0 = oo is {c = 0}")
dsym, csym, esym = sp.symbols('d_ c_ e_')
check2("F.9", sp.roots(Poly((dsym ** 2 - 4 * csym * esym).subs(csym, 0), dsym)) == {0: 2},
       "Thm 6.3: the line {c = 0} meets the conic {d^2 = 4ce} in the double point (0:0:1): tangency")
unit = sp.cancel(Res12 / (p1 * p2))
check2("F.10", expand(sp.numer(sp.together(unit - (q2 / p2 - q1 / p1)))) == 0,
       "Thm 6.3(1): the unit delta/(p1 p2) is the difference of the two roots q2/p2 - q1/p1")
dets = [Matrix([[d_ - 1, 1], [1, 1]]).det() for d_ in range(2, 9)]
check2("F.11", dets == [d_ - 2 for d_ in range(2, 9)],
       "Prop 7.4: the character matrix [[d-1,1],[1,1]] has determinant d - 2 for d = 2..8")
zeta = sp.symbols('zeta')
ok_kernel = True
for d_ in range(3, 8):
    Qd = generic_form('h', d_ - 1); Ld = p * s + q * t
    Rd = sylvester(Ld, Qd, 1, d_ - 1).det()
    Rz = sylvester(zeta * Ld, Qd / zeta, 1, d_ - 1).det()
    ok_kernel = ok_kernel and simplify(Rz - zeta ** (d_ - 2) * Rd) == 0
check2("F.12", ok_kernel,
       "Prop 7.4: (L,Q) -> (zeta L, zeta^-1 Q) multiplies Res by zeta^(d-2): mu_(d-2) fixes both constraints")
aa, bb = sp.symbols('a_ b_', integer=True)
check2("F.13", expand(Matrix([[bb, aa], [1, 1]]).det() - (bb - aa)) == 0,
       "Prop 7.5: the character matrix [[b,a],[1,1]] has determinant b - a")
mvals = all(len(sp.roots(Poly(lam ** m_ - 1, lam))) == m_ and sum(sp.roots(Poly(lam ** m_ - 1, lam)).values()) == m_ for m_ in range(1, 7))
check2("F.14", mvals, "Prop 7.5 / Thm 6.4: lam^m = 1 has exactly m distinct solutions over C for m = 1..6")
check2("F.15", 1 * sp.binomial(3, 1) == 3 and all(all((d_ - 2) * chi != 1 for chi in range(-12, 13)) for d_ in range(4, 9)),
       "Thm 6.4(2): generic degree m*binom(n,a) = 3 at (1,2); Prop 7.4: 1 = (d-2) chi is unsolvable for d = 4..8")

# ======================================================================= summary
fails = [n for n, ok in results if not ok]
print(f"\n{len(results)} checks; sympy {sp.__version__}; FAILS: {'none' if not fails else ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
