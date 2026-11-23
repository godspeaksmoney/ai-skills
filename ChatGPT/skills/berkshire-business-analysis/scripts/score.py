"""Calculate the score and star rating from six evidence-based grades."""

import argparse
import sys
from decimal import Decimal, ROUND_HALF_UP


WEIGHTS = (25, 20, 15, 10, 15, 15)
LOWER_BOUNDS = (1, 40, 55, 70, 85)


def grade(value):
    try:
        result = Decimal(value)
    except ArithmeticError as error:
        raise argparse.ArgumentTypeError("expected a grade from 0 to 5") from error
    if not result.is_finite() or not 0 <= result <= 5 or result % Decimal("0.5"):
        raise argparse.ArgumentTypeError("expected a grade from 0 to 5 in half points")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "grades",
        type=grade,
        nargs=6,
        help="moat, owner earnings, capital allocation, management, resilience, price",
    )
    inputs = parser.parse_args().grades
    contributions = [weight * result / 5 for weight, result in zip(WEIGHTS, inputs)]
    score = max(1, int(sum(contributions).quantize(Decimal("1"), rounding=ROUND_HALF_UP)))
    stars = sum(score >= bound for bound in LOWER_BOUNDS)
    print("Points: " + ", ".join(f"{points:.1f}" for points in contributions))
    visual_rating = "★" * stars + "☆" * (5 - stars)
    try:
        visual_rating.encode(sys.stdout.encoding or "utf-8")
    except UnicodeEncodeError:
        visual_rating = "*" * stars + "-" * (5 - stars)
    print(f"{score}/100 | {visual_rating} ({stars} of 5)")


if __name__ == "__main__":
    main()
