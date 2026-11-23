#!/usr/bin/env python3
"""Generic scenario equity DCF with a market-implied solve.

Revenue model:  core_revenue_t = core_revenue_0 x prod(1 + market_growth_1..t) x share_t x price_t
Other revenue, cash costs and cash investment grow at their own rates.
FCF_t = (core + other - cost) x (1 - tax) - investment; Gordon terminal value after the last year.
Equity = PV(FCF) + PV(TV) + bridge (non-operating assets net of debt and other claims).

Usage:
  python scripts/scenario_dcf.py config.json            # values, weighted value, gap
  python scripts/scenario_dcf.py config.json --solve    # flat market growth implied by price (base case)
See the example at the bottom of this file (`--example` prints it).
"""
import argparse
import json

EXAMPLE = {
    "price": 50.0, "shares": 100.0, "cost_of_equity": 0.11, "tax": 0.25, "bridge": 400.0,
    "year0": {"core_revenue": 1000.0, "other_revenue": 50.0, "cash_cost": 400.0, "cash_investment": 60.0},
    "growth": {"other_revenue": 0.06, "cash_cost": 0.06, "cash_investment": 0.06},
    "base_case": "base",
    "scenarios": {
        "bear": {"p": 0.3, "market_growth": [0.04] * 5, "share": [1, .97, .94, .92, .90], "price": [1, .98, .96, .95, .95], "terminal_growth": 0.03},
        "base": {"p": 0.5, "market_growth": [0.07] * 5, "share": [1] * 5, "price": [1] * 5, "terminal_growth": 0.04},
        "bull": {"p": 0.2, "market_growth": [0.10] * 5, "share": [1, 1.01, 1.02, 1.03, 1.04], "price": [1] * 5, "terminal_growth": 0.045},
    },
}


def value(cfg, s, market_growth=None, ke=None, tg=None):
    y0, gr = cfg["year0"], cfg["growth"]
    ke = cfg["cost_of_equity"] if ke is None else ke
    tg = s["terminal_growth"] if tg is None else tg
    mg = market_growth or s["market_growth"]
    if ke <= tg:
        raise ValueError("cost of equity must exceed terminal growth")
    cum, pv, fcf = 1.0, 0.0, 0.0
    for t in range(1, len(mg) + 1):
        cum *= 1 + mg[t - 1]
        core = y0["core_revenue"] * cum * s["share"][t - 1] * s["price"][t - 1]
        other = y0["other_revenue"] * (1 + gr["other_revenue"]) ** t
        cost = y0["cash_cost"] * (1 + gr["cash_cost"]) ** t
        inv = y0["cash_investment"] * (1 + gr["cash_investment"]) ** t
        fcf = (core + other - cost) * (1 - cfg["tax"]) - inv
        pv += fcf / (1 + ke) ** t
    n = len(mg)
    pv_tv = fcf * (1 + tg) / (ke - tg) / (1 + ke) ** n
    return (pv + pv_tv + cfg["bridge"]) / cfg["shares"]


def solve(cfg):
    s = cfg["scenarios"][cfg["base_case"]]
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = value(cfg, s, market_growth=[mid] * len(s["market_growth"]))
        lo, hi = (mid, hi) if v < cfg["price"] else (lo, mid)
    return mid


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config", nargs="?")
    ap.add_argument("--solve", action="store_true")
    ap.add_argument("--example", action="store_true")
    a = ap.parse_args()
    if a.example or not a.config:
        print(json.dumps(EXAMPLE, indent=2))
        return
    cfg = json.load(open(a.config, encoding="utf-8"))
    tot_p = sum(s["p"] for s in cfg["scenarios"].values())
    if abs(tot_p - 1) > 1e-9:
        raise SystemExit(f"Scenario probabilities sum to {tot_p}, not 1.")
    w = 0.0
    for k, s in cfg["scenarios"].items():
        v = value(cfg, s)
        w += s["p"] * v
        print(f"{k:<6} p={s['p']:.0%}  value/share={v:.2f}")
    print(f"weighted={w:.2f}  price={cfg['price']:.2f}  gap={w / cfg['price'] - 1:+.1%}")
    if a.solve:
        print(f"implied flat market growth (base case otherwise unchanged): {solve(cfg):.2%}")


if __name__ == "__main__":
    main()
