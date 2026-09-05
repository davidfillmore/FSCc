#!/usr/bin/env python3
"""Generate the wiki figures as SVG (no dependencies beyond the standard library).

Run from the repository root:  python3 tools/make-figures.py
Writes figures/<name>.svg and, if the sibling wiki clone ../FSCc.wiki exists,
copies each figure to ../FSCc.wiki/images/<name>.svg for the wiki to serve.

Figure 1, power-of-a-point.svg: Kisil's elliptic model of a cycle on the line
is the semicircle on the point-pair; the power of a point is the squared
tangent length (Theorem 3.3 of the wiki). Panel data are exact:
  left   : Q = u^2 - 1 (roots -1, 1), u = 2, power 3 = t^2
  middle : the zero-radius limit disc -> 0 and the point-cycle Z(u0)
  right  : Q = u(u - 3/2), u = 2: power (2)(1/2) = 1, the stratum Res = 1
"""
import html
import math
import shutil
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
WIKI_IMG = ROOT.parent / "FSCc.wiki" / "images"

W, H = 1320, 310          # canvas: three 400-px panels with 30-px gaps
PW, PH = 400, 200         # panel size
GAP = 30
TOP = 60                  # panel top (room for titles)

BLUE, RED, GREEN, GRAY, INK = "#1f5fbf", "#c8102e", "#2a9d5c", "#8a8a8a", "#222"
FONT = "font-family='Helvetica, Arial, sans-serif'"


def fmt(s: str, size: float = 14) -> str:
    """Escape text for SVG and turn X_{sub} into a subscript tspan (absolute sizes:
    percentage font sizes inside tspans render wrongly in some rasterizers)."""
    out, i = [], 0
    sub, shift = f"{size * 0.72:.1f}", f"{size * 0.30:.1f}"
    while i < len(s):
        j = s.find("_{", i)
        if j < 0:
            out.append(html.escape(s[i:])); break
        k = s.find("}", j)
        out.append(html.escape(s[i:j]))
        out.append(f"<tspan dy='{shift}' font-size='{sub}'>{html.escape(s[j + 2:k])}</tspan>"
                   f"<tspan dy='-{shift}'></tspan>")
        i = k + 1
    return "".join(out)


class Panel:
    """Map a window u in [umin, umax], v in [0, vmax] onto a panel."""

    def __init__(self, x0, umin, umax, vmax, pw=None, y_axis=None):
        self.x0, self.umin, self.umax, self.vmax = x0, umin, umax, vmax
        self.pw = pw or PW
        self.scale = self.pw / (umax - umin)
        self.y_axis = y_axis if y_axis is not None else TOP + PH - 60   # pixel row of the real line

    def X(self, u):
        return self.x0 + (float(u) - self.umin) * self.scale

    def Y(self, v):
        return self.y_axis - float(v) * self.scale

    def axis(self):
        return (f"<line x1='{self.x0}' y1='{self.y_axis}' x2='{self.x0 + self.pw}' y2='{self.y_axis}' "
                f"stroke='{INK}' stroke-width='1.4'/>"
                f"<text x='{self.x0 + self.pw - 2}' y='{self.y_axis - 8}' font-size='13' fill='{INK}' "
                f"text-anchor='end' {FONT}>the real line</text>")

    def semicircle(self, a, b, color=BLUE, width=2.0, opacity=1.0, dash=""):
        a, b = float(a), float(b)
        r = (b - a) / 2 * self.scale
        d = f" stroke-dasharray='{dash}'" if dash else ""
        return (f"<path d='M {self.X(a)} {self.y_axis} A {r} {r} 0 0 1 {self.X(b)} {self.y_axis}' "
                f"fill='none' stroke='{color}' stroke-width='{width}' opacity='{opacity}'{d}/>")

    def dot(self, u, v=0, color=RED, r=4.5, hollow=False):
        fill = "white" if hollow else color
        return (f"<circle cx='{self.X(u)}' cy='{self.Y(v)}' r='{r}' fill='{fill}' "
                f"stroke='{color}' stroke-width='1.8'/>")

    def seg(self, u1, v1, u2, v2, color=GREEN, width=2.0, dash=""):
        d = f" stroke-dasharray='{dash}'" if dash else ""
        return (f"<line x1='{self.X(u1)}' y1='{self.Y(v1)}' x2='{self.X(u2)}' y2='{self.Y(v2)}' "
                f"stroke='{color}' stroke-width='{width}'{d}/>")

    def text(self, u, v, s, size=14, color=INK, anchor="middle", dx=0, dy=0, italic=False):
        style = " font-style='italic'" if italic else ""
        return (f"<text x='{self.X(u) + dx}' y='{self.Y(v) + dy}' font-size='{size}' fill='{color}' "
                f"text-anchor='{anchor}'{style} {FONT}>{fmt(s, size)}</text>")

    def title(self, s):
        return (f"<text x='{self.x0 + self.pw / 2}' y='{TOP - 22}' font-size='16' font-weight='bold' "
                f"fill='{INK}' text-anchor='middle' {FONT}>{html.escape(s)}</text>")

    def caption(self, lines, size=13):
        out = []
        for i, s in enumerate(lines):
            out.append(f"<text x='{self.x0}' y='{self.y_axis + 44 + 18 * i}' font-size='{size}' "
                       f"fill='{INK}' {FONT}>{fmt(s, size)}</text>")
        return "".join(out)

    def circle(self, cu, cv, r, color=BLUE, width=1.6, opacity=1.0, dash=""):
        """Full circle with centre (cu, cv) and radius r in window units."""
        d = f" stroke-dasharray='{dash}'" if dash else ""
        return (f"<circle cx='{self.X(cu)}' cy='{self.Y(cv)}' r='{r * self.scale}' fill='none' "
                f"stroke='{color}' stroke-width='{width}' opacity='{opacity}'{d}/>")

    def arc_through(self, k, color=BLUE, width=1.6, opacity=1.0):
        """Upper arc of the circle centred (0, k) through (-1, 0) and (1, 0)."""
        r = math.sqrt(1 + k * k) * self.scale
        large = 1 if k > 0 else 0
        return (f"<path d='M {self.X(-1)} {self.Y(0)} A {r} {r} 0 {large} 1 {self.X(1)} {self.Y(0)}' "
                f"fill='none' stroke='{color}' stroke-width='{width}' opacity='{opacity}'/>")

    def ray(self, angle_deg, length, color=BLUE, width=1.6, opacity=1.0, origin=(0, 0)):
        a = math.radians(angle_deg)
        u0, v0 = origin
        return self.seg(u0, v0, u0 + length * math.cos(a), v0 + length * math.sin(a), color=color, width=width) \
            .replace("/>", f" opacity='{opacity}'/>")

    def arrowhead(self, u, v, direction_deg, color=BLUE, size=7):
        """Small triangle at window point (u, v) pointing along direction_deg (window angle)."""
        a = math.radians(direction_deg)
        dx, dy = math.cos(a), math.sin(a)             # window direction
        px, py = self.X(u), self.Y(v)
        # pixel direction (y flipped)
        ex, ey = dx, -dy
        nx, ny = -ey, ex
        tip = (px + ex * size * 0.6, py + ey * size * 0.6)
        base1 = (px - ex * size * 0.6 + nx * size * 0.5, py - ey * size * 0.6 + ny * size * 0.5)
        base2 = (px - ex * size * 0.6 - nx * size * 0.5, py - ey * size * 0.6 - ny * size * 0.5)
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (tip, base1, base2))
        return f"<polygon points='{pts}' fill='{color}'/>"

    def double_dot(self, u, color=BLUE):
        return (f"<circle cx='{self.X(u)}' cy='{self.Y(0)}' r='7' fill='none' stroke='{color}' stroke-width='1.8'/>"
                f"<circle cx='{self.X(u)}' cy='{self.Y(0)}' r='3.5' fill='{color}'/>")


def tangent_point(c, r, u):
    """Tangent point on the circle (centre (c,0), radius r) from the external point (u,0), u > c."""
    c, r, u = float(c), float(r), float(u)
    cos = r / (u - c)
    return c + r * cos, r * math.sqrt(1 - cos * cos)


def right_angle_mark(P, c, r, T, size=0.09):
    """Small square at the tangent point T marking radius ⟂ tangent."""
    tx, ty = T
    # unit vectors: along radius (outward) and along tangent (towards the external point)
    rx, ry = (tx - c) / r, ty / r
    ux, uy = ry, -rx
    s = size
    p1 = (tx - rx * s, ty - ry * s)
    p2 = (p1[0] + ux * s, p1[1] + uy * s)
    p3 = (tx + ux * s, ty + uy * s)
    pts = " ".join(f"{P.X(x)},{P.Y(y)}" for x, y in (p1, p2, p3))
    return f"<polyline points='{pts}' fill='none' stroke='{GRAY}' stroke-width='1'/>"


def figure_power_of_a_point() -> str:
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>",
             f"<rect width='{W}' height='{H}' fill='white'/>"]

    # ---------------- panel 1: the power as a squared tangent length
    P = Panel(GAP, -2.2, 3.0, 2.2)
    a, b, u = Fr(-1), Fr(1), Fr(2)
    c, r = (a + b) / 2, (b - a) / 2
    power = (u - a) * (u - b)                      # exact: 3
    T = tangent_point(c, r, u)
    parts += [P.title("Power of a point with respect to a cycle"), P.axis(),
              P.semicircle(a, b),
              P.seg(c, 0, T[0], T[1], color=GRAY, width=1.2, dash="4 3"),        # radius
              P.seg(u, 0, T[0], T[1], color=GREEN, width=2.4),                    # tangent
              right_angle_mark(P, c, r, T),
              P.dot(a, color=BLUE), P.dot(b, color=BLUE), P.dot(u), P.dot(c, color=GRAY, r=3),
              P.text(a, 0, "a", dy=22, italic=True), P.text(b, 0, "b", dy=22, italic=True),
              P.text(u, 0, "u", dy=22, italic=True, color=RED),
              P.text(c, 0, "c", dy=22, italic=True, color=GRAY),
              P.text((float(c) + T[0]) / 2, T[1] / 2, "r", dx=-11, dy=4, italic=True, color=GRAY, size=13),
              P.text((float(u) + T[0]) / 2, T[1] / 2, "t", dx=12, dy=-6, italic=True, color=GREEN),
              P.text(c, 0, "the cycle {a, b}: Q(u) = (u − a)(u − b)", dy=-float(r) * P.scale - 12,
                     color=BLUE, size=13),
              P.caption(["pow(u) = Q(u) = |u − c|² − r² = t²",
                         f"here a = −1, b = 1, u = 2: pow = {power}, t = √3",
                         "pow = 0 iff u lies on the cycle; pow < 0 between a and b"])]

    # ---------------- panel 2: the zero-radius limit and the point-cycle
    P = Panel(GAP + PW + GAP, -2.2, 3.0, 2.2)
    parts += [P.title("Zero-radius cycles are points"), P.axis()]
    for k, half in enumerate((Fr(1), Fr(3, 5), Fr(3, 10), Fr(1, 10))):
        parts.append(P.semicircle(-half, half, opacity=1.0 - 0.2 * k, width=2.0 - 0.3 * k))
    parts += [P.dot(0, color=BLUE, r=5),
              P.text(0, 0, "Z(u₀): the point-cycle, det = 0", dy=24, color=BLUE, size=13),
              P.text(0, Fr(1), "disc Q = (b − a)² shrinks to 0", dy=-14, color=BLUE, size=13),
              P.caption(["Two roots collide: the semicircle shrinks to the",
                         "null vector L², the zero-radius cycle of the root.",
                         "Pairing a cycle with a point-cycle evaluates Q there."])]

    # ---------------- panel 3: the unit-power stratum Res = 1
    P = Panel(GAP + 2 * (PW + GAP), -1.2, 4.0, 2.2)
    a, b, u = Fr(0), Fr(3, 2), Fr(2)
    c, r = (a + b) / 2, (b - a) / 2
    power = (u - a) * (u - b)                      # exact: 1
    assert power == 1 and (u - c) ** 2 - r ** 2 == 1
    T = tangent_point(c, r, u)                     # (6/5, 3/5), tangent length exactly 1
    parts += [P.title("Tao's stratum Res(L, Q) = 1: unit power"), P.axis(),
              P.semicircle(a, b),
              P.seg(c, 0, T[0], T[1], color=GRAY, width=1.2, dash="4 3"),
              P.seg(u, 0, T[0], T[1], color=GREEN, width=2.4),
              right_angle_mark(P, c, r, T),
              P.dot(a, color=BLUE), P.dot(b, color=BLUE), P.dot(u), P.dot(c, color=GRAY, r=3),
              P.text(a, 0, "0", dy=22), P.text(b, 0, "3/2", dy=22), P.text(u, 0, "u = 2", dy=22, color=RED),
              P.text((float(u) + T[0]) / 2, T[1] / 2, "t = 1", dx=16, dy=-4, color=GREEN),
              P.text(c, 0, "Q = u(u − 3/2)", dy=-float(r) * P.scale - 12, color=BLUE, size=13),
              P.text(Fr(29, 10), Fr(2, 5), "L = s − 2t", color=RED, size=13, anchor="start"),
              P.caption(["Res(L, Q) = Q(2) = (2)(1/2) = 1: the point of L",
                         "sits at unit power from the point-pair of Q.",
                         "Res = 0 is incidence: the ramification divisor."])]

    parts.append("</svg>")
    return "\n".join(parts)


def figure_eph() -> str:
    """Figure 2: the three kinds of one-parameter subgroup of SL2(R) on the upper
    half-plane, drawn as the three classical pencils of circles; the hyperbolic
    panel is the stabilizer torus of the counterexample's slicing datum."""
    Wc, Hc = 1320, 440
    y_axis = 330
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{Wc}' height='{Hc}' viewBox='0 0 {Wc} {Hc}'>",
             f"<rect width='{Wc}' height='{Hc}' fill='white'/>"]
    win = (-2.6, 2.6, 3.6)

    # elliptic: hyperbolic circles about i, Euclidean centre (0, cosh r), radius sinh r
    P = Panel(GAP, *win, y_axis=y_axis)
    parts += [P.title("Elliptic: a rotation, no fixed point on the line"), P.axis()]
    for k, rho in enumerate((0.45, 0.85, 1.15)):
        c, r = math.cosh(rho), math.sinh(rho)
        parts += [P.circle(0, c, r, opacity=1.0 - 0.22 * k), P.arrowhead(0, c + r, 180)]
    parts += [P.dot(0, 1, color=BLUE, r=4), P.text(0, 1, "i", dx=12, dy=4, italic=True, color=BLUE),
              P.caption(["Orbits of the subgroup fixing the interior point i:",
                         "the circles about i. Both fixed points are conjugate,",
                         "off the line: Kisil's elliptic case, Shaska's definite signs."])]

    # parabolic: horocycles at 0, circles tangent to the line at 0
    P = Panel(GAP + PW + GAP, *win, y_axis=y_axis)
    parts += [P.title("Parabolic: one fixed point"), P.axis()]
    for k, h in enumerate((0.35, 0.75, 1.2, 1.7)):
        parts += [P.circle(0, h, h, opacity=1.0 - 0.18 * k), P.arrowhead(0, 2 * h, 0)]
    parts += [P.dot(0, color=BLUE), P.text(0, 0, "0", dy=22, color=BLUE),
              P.caption(["Orbits of the unipotent subgroup fixing the single",
                         "boundary point 0: the horocycles at 0.",
                         "One fixed point on the line: the parabolic case."])]

    # hyperbolic: the pencil through -1 and 1
    P = Panel(GAP + 2 * (PW + GAP), *win, y_axis=y_axis)
    parts += [P.title("Hyperbolic: a boost, two fixed points"), P.axis()]
    for k, kk in enumerate((-1.4, -0.55, 0.0, 0.7, 1.4)):
        top = kk + math.sqrt(1 + kk * kk)
        parts += [P.arc_through(kk, width=2.2 if kk == 0 else 1.6, opacity=1.0 if kk == 0 else 0.75),
                  P.arrowhead(0, top, 0)]
    parts += [P.double_dot(-1), P.dot(1, color=BLUE),
              P.text(-1, 0, "double root", dy=22, color=BLUE, size=12),
              P.text(1, 0, "simple root", dy=22, color=BLUE, size=12),
              P.caption(["Orbits of the torus fixing two boundary points: the",
                         "arcs through them. The stabilizer of the slicing datum",
                         "fixes its double and its simple root: the counterexample's grading."])]
    parts.append("</svg>")
    return "\n".join(parts)


def figure_three_to_one() -> str:
    """Figure 3: a point-triple splits three ways into a point and a pair.
    Triple -1, 1/2, 2; each split drawn as the pair's semicircle and the point."""
    Wc, Hc = 1320, 320
    y_axis = 200
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{Wc}' height='{Hc}' viewBox='0 0 {Wc} {Hc}'>",
             f"<rect width='{Wc}' height='{Hc}' fill='white'/>"]
    roots = (Fr(-1), Fr(1, 2), Fr(2))
    splits = [(roots[0], (roots[1], roots[2])), (roots[1], (roots[0], roots[2])), (roots[2], (roots[0], roots[1]))]
    titles = ("Split 1: point −1, pair {1/2, 2}", "Split 2: point 1/2, pair {−1, 2}", "Split 3: point 2, pair {−1, 1/2}")
    for i, ((u, (a, b)), title) in enumerate(zip(splits, titles)):
        P = Panel(GAP + i * (PW + GAP), -2.2, 3.2, 2.2, y_axis=y_axis)
        c, r = (a + b) / 2, (b - a) / 2
        power = (u - a) * (u - b)
        parts += [P.title(title), P.axis(), P.semicircle(a, b)]
        if power > 0:
            T = tangent_point(c, r, u) if u > c else None
            if T is None:                      # point to the left of the pair: reflect
                Tx, Ty = tangent_point(-c, r, -u)
                T = (-Tx, Ty)
            parts += [P.seg(u, 0, T[0], T[1], color=GREEN, width=2.2), right_angle_mark(P, c, r, T)]
        for rt in roots:
            parts.append(P.dot(rt, color=BLUE) if rt != u else P.dot(rt))
        for rt, lab in zip(roots, ("−1", "1/2", "2")):
            parts.append(P.text(rt, 0, lab, dy=22, color=RED if rt == u else INK))
        def num(x):
            return str(x).replace("-", "−")
        def factor(x):
            return f"(u + {num(-x)})" if x < 0 else f"(u − {num(x)})"
        sign = "outside the pair: pow > 0" if power > 0 else "between the pair: pow < 0"
        parts += [P.text(c, r, f"Q = {factor(a)}{factor(b)}", dy=-12, color=BLUE, size=13),
                  P.caption([f"pow = Q({num(u)}) = {num(power)}, the point {sign};",
                             "the scaling (λL, λ⁻¹Q) multiplies Res by λ, so exactly",
                             "one λ puts this split on the stratum Res = 1."])]
    parts.append("</svg>")
    return "\n".join(parts)


def figure_three_detectors() -> str:
    """Figure 4: the three root patterns of the slicing cubic and their little groups."""
    Wc, Hc = 1320, 440
    y_axis = 330
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{Wc}' height='{Hc}' viewBox='0 0 {Wc} {Hc}'>",
             f"<rect width='{Wc}' height='{Hc}' fill='white'/>"]
    win = (-2.6, 2.6, 3.6)

    # (3): triple root at 0, Borel little group: dilations at 0 (rays) and horocycles at 0
    P = Panel(GAP, *win, y_axis=y_axis)
    parts += [P.title("Triple root (3): osculating detector"), P.axis()]
    for h in (0.5, 1.1):
        parts += [P.circle(0, h, h, color=BLUE, opacity=0.5), P.arrowhead(0, 2 * h, 0)]
    for ang in (35, 65, 90, 115, 145):
        L = 3.2 / math.sin(math.radians(ang)) if ang != 90 else 3.2
        L = min(L, 3.0)
        parts += [P.ray(ang, L, color=BLUE, opacity=0.8),
                  P.arrowhead(L * math.cos(math.radians(ang)), L * math.sin(math.radians(ang)), ang)]
    parts += [P.double_dot(0), P.text(0, 0, "0, a triple root", dy=24, color=BLUE, size=12),
              P.caption(["Stabilizer of s³ up to scalar: β = 0, a Borel subgroup",
                         "(dimension 2): every map fixing 0. Contains the",
                         "torus and a unipotent subgroup. Slice: punctured line × plane, not affine space."])]

    # (2,1): double root at 0, simple root at infinity: the torus
    P = Panel(GAP + PW + GAP, *win, y_axis=y_axis)
    parts += [P.title("Double and simple root (2,1): tangent detector"), P.axis()]
    for ang in (30, 55, 90, 125, 150):
        L = min(3.2 / math.sin(math.radians(ang)), 3.0)
        parts += [P.ray(ang, L, color=BLUE, opacity=0.85),
                  P.arrowhead(L * math.cos(math.radians(ang)), L * math.sin(math.radians(ang)), ang)]
    parts += [P.double_dot(0), P.text(0, 0, "0, the double root", dy=24, color=BLUE, size=12),
              P.text(0, 3.25, "∞, the simple root", dy=-6, color=BLUE, size=12),
              P.caption(["Stabilizer of s²t up to scalar: β = γ = 0, the torus T,",
                         "the boost fixing 0 and ∞: weights (2, −2, −4), i.e. (1, −1, −2).",
                         "Slice: affine space, the counterexample."])]

    # (1,1,1): three distinct roots -1, 0, 1: finite anharmonic group
    P = Panel(GAP + 2 * (PW + GAP), *win, y_axis=y_axis)
    parts += [P.title("Three distinct roots (1,1,1): transverse detector"), P.axis()]
    # the swap of -1 and 1 (an involution) and a 3-cycle, drawn as dashed arcs
    parts += [P.arc_through(0.0, color=GRAY, width=1.4).replace("/>", " stroke-dasharray='5 4'/>"),
              P.arrowhead(0, 1, 180, color=GRAY)]
    for (a, b) in ((-1, 0), (0, 1)):
        c, r = (a + b) / 2, (b - a) / 2
        parts += [P.semicircle(a, b, color=GRAY, width=1.4, dash="5 4"), P.arrowhead(c, r, 0, color=GRAY)]
    for rt, lab in ((-1, "−1"), (0, "0"), (1, "1")):
        parts += [P.dot(rt, color=BLUE), P.text(rt, 0, lab, dy=22, color=BLUE)]
    parts += [P.text(0, 1.15, "a 3-cycle of the roots", dy=-4, color=GRAY, size=12),
              P.caption(["Stabilizer of st(s − t) up to scalar: the anharmonic group",
                         "S₃ permuting the three roots (3-cycles and swaps), finite: no",
                         "one-parameter subgroup, no grading. Slice: not affine space (χ = 0)."])]
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    figs = {"power-of-a-point": figure_power_of_a_point(),
            "eph-trichotomy": figure_eph(),
            "three-to-one": figure_three_to_one(),
            "three-detectors": figure_three_detectors()}
    for name, svg in figs.items():
        path = OUT / f"{name}.svg"
        path.write_text(svg, encoding="utf-8")
        print("wrote", path.relative_to(ROOT), f"({len(svg)} bytes)")
        if WIKI_IMG.parent.exists():
            WIKI_IMG.mkdir(exist_ok=True)
            shutil.copy(path, WIKI_IMG / path.name)
            print("copied to", WIKI_IMG / path.name)


if __name__ == "__main__":
    main()
