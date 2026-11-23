#!/usr/bin/env python3
"""Compute the skill's 1-100 score, star display and near-threshold range.

Usage:
  python scripts/score.py 4.5 2.5 3.5 3.5 4.0 1.0
  python scripts/score.py --gap -0.211          # valuation starting grade for a value gap
Grades follow rubric order: current economics, durability, reinvestment,
capital allocation & governance, financial resilience, expectations & valuation.
Weights, grade scale, bands and stars are skill choices (see references/scoring.md).
"""
import argparse
from decimal import Decimal, ROUND_HALF_UP

WEIGHTS = [20, 25, 15, 10, 10, 20]
NAMES = ["Current economics", "Durability of competitive advantage", "Profitable reinvestment",
         "Capital allocation and governance", "Financial resilience",
         "Expectations and valuation at the observed price"]
GAP_BANDS = [(-0.35, 0), (-0.15, 1), (-0.05, 2), (0.10, 3), (0.25, 4)]


def stars(score):
    n = 1 if score <= 20 else 2 if score <= 40 else 3 if score <= 60 else 4 if score <= 80 else 5
    return "★" * n + "☆" * (5 - n)


def total(grades):
    pts = [Decimal(str(w)) * Decimal(str(g)) / 5 for w, g in zip(WEIGHTS, grades)]
    raw = sum(pts)
    return pts, raw, max(1, int(raw.quantize(Decimal("1"), rounding=ROUND_HALF_UP)))


def check(grades):
    if len(grades) != 6:
        raise SystemExit("Provide six grades in rubric order.")
    for g in grades:
        if g < 0 or g > 5 or (g * 2) != int(g * 2):
            raise SystemExit(f"Grade {g} must be 0-5 in half-point steps.")


def valuation_grade(gap):
    for upper, grade in GAP_BANDS:
        if gap < upper:
            return grade
    return 5


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("grades", nargs="*", type=float)
    ap.add_argument("--gap", type=float, help="probability-weighted value / price - 1")
    a = ap.parse_args()
    if a.gap is not None:
        print(f"Value gap {a.gap:+.1%} -> starting valuation grade {valuation_grade(a.gap)}")
        if not a.grades:
            return
    check(a.grades)
    pts, raw, score = total(a.grades)
    for n, w, g, p in zip(NAMES, WEIGHTS, a.grades, pts):
        print(f"{n:<50} w={w:>2}  grade={g:<4} points={float(p):g}")
    print(f"Unrounded {float(raw):g} -> score {score}/100 · {stars(score)}")
    lo, hi = score, score
    for i in range(6):
        for d in (-0.5, 0.5):
            g = list(a.grades)
            g[i] = min(5, max(0, g[i] + d))
            s = total(g)[2]
            lo, hi = min(lo, s), max(hi, s)
    if stars(lo) != stars(hi):
        print(f"Near threshold: plausible {lo}-{hi} ({stars(lo)} to {stars(hi)}) from a ±0.5 change in one grade")


if __name__ == "__main__":
    main()
