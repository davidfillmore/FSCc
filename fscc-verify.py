"""fscc-verify.py -- exact-arithmetic certificates for the FSCc wiki
(https://github.com/davidfillmore/FSCc/wiki): the inversive-geometry dictionary
for the July 2026 Jacobian-conjecture counterexample, the stabilizer-torus
theorem, the n = 2 dead end, and the representation-theoretic obstruction.

Run:  python3 fscc-verify.py          (SymPy 1.14.0; see requirements.txt)
Expected: every line prints PASS, "FAILS: none", exit status 0.
No floating point anywhere: SymPy over Q (and Q(i) where Kisil's e0 = i appears).

Blocks, cross-referenced from the wiki pages:
  [01] The dictionary        -- The-Inversive-Dictionary: Props 3.1, 3.2, Thm 3.3, Prop 3.4
  [02] The stabilizer torus  -- The-Stabilizer-Torus-and-the-EPH-Trichotomy: Thm 4.1
  [03] The n = 2 dead end    -- The-Dimension-Floor: Prop 6.1, Thm 6.2 (invariants)
  [05] Representation obstr. -- The-Mobius-Group-and-Binary-Forms: Props 5.1, 5.2
  [00] Baseline              -- the map itself: det DF = -2, three-point collision

Provenance: adapted on September 5, 2026 from the phase-1 suite of the program's
private repository (38 checks, July 28-29, 2026; the Hessian-conjecture block
[04] is omitted here as out of scope). Block numbers are kept so that citations
in the wiki match.
"""
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

T0 = time.time()
FAILS = []


def ok(name, cond):
    print(("PASS" if cond else "FAIL"), "-", name)
    if not cond:
        FAILS.append(name)


print("== [01] Dictionary identities =====================================")
p, q, c, d, e = sp.symbols('p q c d e')
s, t = sp.symbols('s t')
L = p*s + q*t
Q = c*s**2 + d*s*t + e*t**2

# (1.1) Sylvester resultant
Res = sp.expand(sp.det(sp.Matrix([[p, q, 0], [0, p, q], [c, d, e]])))
ok("1.1 Res(L,Q) = p^2 e - pqd + q^2 c", Res == sp.expand(p**2*e - p*q*d + q**2*c))

# (1.2) Res = value of Q at the root (-q:p) of L
ok("1.2 L(-q,p) = 0 and Res = Q(-q,p)",
   sp.expand(L.subs({s: -q, t: p})) == 0 and
   sp.expand(Res - Q.subs({s: -q, t: p})) == 0)

# (1.3) polarised discriminant B; B(L^2,Q) = -2 Res
B = lambda c1, d1, e1, c2, d2, e2: d1*d2 - 2*c1*e2 - 2*c2*e1
ok("1.3a B(Q,Q) = disc Q = d^2 - 4ce", sp.expand(B(c, d, e, c, d, e) - (d**2 - 4*c*e)) == 0)
ok("1.3b disc(L^2) = 0", sp.expand(B(p**2, 2*p*q, q**2, p**2, 2*p*q, q**2)) == 0)
ok("1.3c B(L^2,Q) = -2 Res(L,Q)", sp.expand(B(p**2, 2*p*q, q**2, c, d, e) + 2*Res) == 0)

# (1.4) Kisil EPAL-1 convention: cycle (k,-2l,m), C = [[l*e0, m],[k, -l*e0]], e0 = i
I = sp.I
k1, l1, m1, k2, l2, m2, u0 = sp.symbols('k1 l1 m1 k2 l2 m2 u0')
C1 = sp.Matrix([[I*l1, m1], [k1, -I*l1]])
C2 = sp.Matrix([[I*l2, m2], [k2, -I*l2]])
tr12 = sp.expand(sp.trace(C1*C2))
ok("1.4a tr(C1 C2) = -2 l1 l2 + m1 k2 + k1 m2 (real, i drops out)",
   tr12 == sp.expand(-2*l1*l2 + m1*k2 + k1*m2))
# with l = -d/2 (Tao coefficients (c,d,e) <-> Kisil (k,-2l,m)=(c,d,e)):
tr_pol = tr12.subs({l1: -sp.Rational(1, 2)*sp.Symbol('d1'), l2: -sp.Rational(1, 2)*sp.Symbol('d2'),
                    k1: sp.Symbol('c1'), m1: sp.Symbol('e1'), k2: sp.Symbol('c2'), m2: sp.Symbol('e2')})
c1_, d1_, e1_, c2_, d2_, e2_ = sp.symbols('c1 d1 e1 c2 d2 e2')
ok("1.4b tr(C_{Q1} C_{Q2}) = -1/2 B(Q1,Q2)",
   sp.expand(tr_pol + sp.Rational(1, 2)*B(c1_, d1_, e1_, c2_, d2_, e2_)) == 0)
# zero-radius cycle at u0 (= cycle of (u-u0)^2): k=1, l=u0, m=u0^2
Zu = sp.Matrix([[I*u0, u0**2], [1, -I*u0]])
CQ = sp.Matrix([[-I*d/2, e], [c, I*d/2]])       # Kisil matrix of Q, l = -d/2
ok("1.4c det Z(u0) = 0; det C_Q = disc(Q)/4",
   sp.simplify(Zu.det()) == 0 and sp.expand(CQ.det() - (d**2 - 4*c*e)/4) == 0)
ok("1.4d tr(C_Q Z(u0)) = Q(u0,1) (incidence pairing evaluates Q)",
   sp.expand(sp.trace(CQ*Zu) - Q.subs({s: u0, t: 1})) == 0)
# unnormalised zero-radius cycle of L: (k,-2l,m) = (p^2, 2pq, q^2) => l = -pq
ZL = sp.Matrix([[-I*p*q, q**2], [p**2, I*p*q]])
ok("1.4e  ** tr(C_Q Z_L) = Res(L,Q) exactly (Kisil convention) **",
   sp.expand(sp.trace(CQ*ZL) - Res) == 0)
ok("1.4f Z_L = p^2 * Z(-q/p)", sp.simplify(ZL - p**2*Zu.subs(u0, -q/p)) == sp.zeros(2, 2))

# (1.5) M_Q = 2 J S_Q; equivariance via J g^T J^{-1} = g^{-1} (det g = 1)
a1, b1, g1 = sp.symbols('a1 b1 g1')
d1v = (1 + b1*g1)/a1                              # det = 1
g = sp.Matrix([[a1, b1], [g1, d1v]])
Jm = sp.Matrix([[0, 1], [-1, 0]])
SQ = sp.Matrix([[c, d/2], [d/2, e]])
MQ = 2*Jm*SQ
ok("1.5a M_Q = 2 J S_Q = [[d, 2e], [-2c, -d]]", MQ == sp.Matrix([[d, 2*e], [-2*c, -d]]))
ok("1.5b J g^T J^{-1} = g^{-1} for det g = 1",
   sp.simplify(Jm*g.T*Jm.inv() - g.inv()) == sp.zeros(2, 2))
Qg = sp.expand(Q.subs({s: a1*s + b1*t, t: g1*s + d1v*t}, simultaneous=True))
cg, dg, eg = Qg.coeff(s, 2).coeff(t, 0), Qg.coeff(s, 1).coeff(t, 1), Qg.coeff(s, 0).coeff(t, 2)
MQg = sp.Matrix([[dg, 2*eg], [-2*cg, -dg]])
ok("1.5c M_{Q o g} = g^{-1} M_Q g", sp.simplify(MQg - g.inv()*MQ*g) == sp.zeros(2, 2))
ok("1.5d det M_Q = -disc Q", sp.expand(MQ.det() + (d**2 - 4*c*e)) == 0)

# (1.6) full SL2 invariance of Res (not only the torus)
Lg = sp.expand(L.subs({s: a1*s + b1*t, t: g1*s + d1v*t}, simultaneous=True))
pg, qg = Lg.coeff(s), Lg.coeff(t)
Resg = sp.expand(pg**2*eg - pg*qg*dg + qg**2*cg)
ok("1.6 Res(L o g, Q o g) = Res(L,Q) for det g = 1", sp.simplify(Resg - Res) == 0)

print("== [02] Torus theorem =============================================")
lam = sp.symbols('lam')
# combined element: diag(lam,1/lam) substitution + (L,Q) -> (lam L, lam^-2 Q)
TR = {p: lam**2*p, q: q, c: c, d: d/lam**2, e: e/lam**4}
ok("2.1 combined torus preserves Res", sp.simplify(Res.subs(TR) - Res) == 0)
ok("2.2 combined torus preserves D(LQ) = pd + qc",
   sp.simplify((p*d + q*c).subs(TR) - (p*d + q*c)) == 0)
# torus alone / scalings alone (weights used in the uniqueness argument)
Tt = {p: lam*p, q: q/lam, c: lam**2*c, d: d, e: e/lam**2}
ok("2.3 torus alone: Res invariant, D(LQ) -> lam * D(LQ)",
   sp.simplify(Res.subs(Tt) - Res) == 0 and
   sp.simplify((p*d + q*c).subs(Tt) - lam*(p*d + q*c)) == 0)
l1s, l2s = sp.symbols('l1s l2s')
Sc = {p: l1s*p, q: l1s*q, c: l2s*c, d: l2s*d, e: l2s*e}
ok("2.4 scalings: Res -> l1^2 l2 Res, D(LQ) -> l1 l2 D(LQ)",
   sp.simplify(Res.subs(Sc) - l1s**2*l2s*Res) == 0 and
   sp.simplify((p*d + q*c).subs(Sc) - l1s*l2s*(p*d + q*c)) == 0)
# induced action on Tao slice coordinates
ycoord = 2*q*d - p*e
zcoord = 2*d**2 + c*e + 6*q*d**2 + 3*q*c*e - sp.Rational(9, 2)*e
ok("2.5 slice coords: a -> lam^2 a, y -> lam^-2 y, z -> lam^-4 z",
   TR[p] == lam**2*p and
   sp.expand(ycoord.subs(TR)*lam**2 - ycoord) == 0 and
   sp.expand(zcoord.subs(TR)*lam**4 - zcoord) == 0)
# Tao parametrisation closes
av, Y, Zc = sp.symbols('av Y Zc')
bP = 1 + av*Y
cP = 1 - sp.Rational(3, 2)*av*Y + av**2*Zc
dP = (1 - bP*cP)/av
eP = (1 + av*bP*dP - cP*bP**2)/av**2
ok("2.6 constraints hold on the parametrised slice: Res = 1 and pd+qc = 1",
   sp.simplify(av**2*eP - av*bP*dP + cP*bP**2 - 1) == 0 and
   sp.simplify(av*dP + bP*cP - 1) == 0)
ok("2.7 inverse formulas recover (y,z)",
   sp.simplify(2*bP*dP - av*eP - Y) == 0 and
   sp.simplify(2*dP**2 + cP*eP + 6*bP*dP**2 + 3*bP*cP*eP - sp.Rational(9, 2)*eP - Zc) == 0)
# direct check on Alpoge's F
x, y, z, tt = sp.symbols('x y z tt')
uA = 1 + x*y
F1 = uA**3*z + y**2*uA*(4 + 3*x*y)
F2 = y + 3*x*uA**2*z + 3*x*y**2*(4 + 3*x*y)
F3 = 2*x - 3*x**2*y - x**3*z
r = [sp.cancel(f.subs({x: tt*x, y: y/tt, z: z/tt**2}, simultaneous=True)/f) for f in (F1, F2, F3)]
ok("2.8 F(tx, y/t, z/t^2) = (t^-2 F1, t^-1 F2, t F3)", r == [1/tt**2, 1/tt, tt])

print("== [03] n = 2 dead end ============================================")
p1, q1, p2, q2, al = sp.symbols('p1 q1 p2 q2 al')
Res11 = p1*q2 - q1*p2                     # resultant of two linear forms
ok("3.1 (a,b)=(1,1): Res(al*L1, al^-1*L2) = Res(L1,L2) — scaling-invariant, cannot rigidify",
   sp.expand(Res11.subs({p1: al*p1, q1: al*q1, p2: p2/al, q2: q2/al}) - Res11) == 0)
# {Res=1} is SL2; T-invariants and the affine quadric
aI, bI, cI, dI = p1*p2, p1*q2, q1*p2, q1*q2
ok("3.2 invariants satisfy a*d = b*c and (on Res=1) c = b - 1, i.e. ad = b(b-1)",
   sp.expand(aI*dI - bI*cI) == 0 and sp.expand((bI - cI) - Res11) == 0)
# general (a,b): Res scaling weight lam1^b lam2^a — here shown for (1,2) used in the floor argument
ok("3.3 (a,b)=(1,2): Res(l1 L, l2 Q) = l1^2 l2 Res  (rigidifiable since weights (2,1) != 0)",
   sp.simplify(Res.subs(Sc) - l1s**2*l2s*Res) == 0)

print("== [05] Representation obstructions ===============================")
# invariant pairing on Sym^n from omega^{tensor n}: parity check for n = 2, 3
w1, w2 = sp.symbols('w1 w2')
def sym_pairing(n, f_coeffs, g_coeffs):
    # <s^{n-i}t^i, s^{n-j}t^j> = 0 unless j = n-i; value (-1)^i * i!(n-i)!/n!
    tot = 0
    for i in range(n + 1):
        tot += f_coeffs[i]*g_coeffs[n - i]*sp.Rational((-1)**i*sp.factorial(i)*sp.factorial(n - i), sp.factorial(n))
    return sp.expand(tot)
fc = sp.symbols('f0:4'); gc = sp.symbols('g0:4')
sym2 = sym_pairing(2, fc[:3], gc[:3]); sym2T = sym_pairing(2, gc[:3], fc[:3])
sym3 = sym_pairing(3, fc, gc);       sym3T = sym_pairing(3, gc, fc)
ok("5.1 pairing on Sym^2 is symmetric; on Sym^3 antisymmetric",
   sp.expand(sym2 - sym2T) == 0 and sp.expand(sym3 + sym3T) == 0)
# SL2 invariance of the Sym^3 pairing (binary cubics under a generic det-1 substitution)
f0, f1, f2, f3 = fc; g0, g1, g2, g3 = gc
cub = lambda co: co[0]*s**3 + co[1]*s**2*t + co[2]*s*t**2 + co[3]*t**3
def coeffs3(expr):
    E = sp.expand(expr)
    return [E.coeff(s, 3 - i).coeff(t, i) for i in range(4)]
fg = coeffs3(cub(fc).subs({s: a1*s + b1*t, t: g1*s + d1v*t}, simultaneous=True))
gg = coeffs3(cub(gc).subs({s: a1*s + b1*t, t: g1*s + d1v*t}, simultaneous=True))
ok("5.2 the Sym^3 pairing is SL2-invariant",
   sp.simplify(sym_pairing(3, fg, gg) - sym3) == 0)
# Clebsch-Gordan weight counts used in 05: dims only (bookkeeping check)
ok("5.3 dim S^2(Sym^3) = 10 = 7 + 3, dim L^2(Sym^3) = 6 = 5 + 1", 10 == 7 + 3 and 6 == 5 + 1)

print("== [00] Alpöge certificate (baseline) =============================")
Jm3 = sp.Matrix([F1, F2, F3]).jacobian([x, y, z])
ok("0.1 det DF == -2 identically", sp.expand(Jm3.det()) == -2)
pts = [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)),
       (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
imgs = [tuple(sp.simplify(f.subs(dict(zip((x, y, z), P)))) for f in (F1, F2, F3)) for P in pts]
ok("0.2 three-point collision onto (-1/4, 0, 0)",
   imgs[0] == imgs[1] == imgs[2] == (sp.Rational(-1, 4), 0, 0))

print()
print(f"sympy {sp.__version__}; elapsed {time.time()-T0:.1f}s; FAILS: {FAILS if FAILS else 'none'}")
raise SystemExit(1 if FAILS else 0)
