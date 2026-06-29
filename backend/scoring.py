def clamp(value, low=0, high=100):
    return max(low, min(high, int(value)))


def flag_dilution_risk(text: str) -> str:
    terms = ["atm", "s-1", "f-1", "424b", "reverse split", "nasdaq deficiency", "going concern", "convertible note", "warrant"]
    lower = text.lower()
    hits = [term for term in terms if term in lower]
    if len(hits) >= 2:
        return "High"
    if hits:
        return "Medium"
    return "Low"


def build_trade_plan(price: float, risk: str):
    stop_pct = 0.06 if risk == "Low" else 0.10 if risk == "Medium" else 0.18
    return {
        "entry": round(price, 4),
        "stop": round(price * (1 - stop_pct), 4),
        "target_1": round(price * 1.15, 4),
        "target_2": round(price * 1.28, 4),
    }


def score_panic_reversal(rvol=5, rsi=30, vwap_reclaim=False, higher_lows=False):
    score = 35 + rvol * 4 + (30 - min(rsi, 30)) + (15 if vwap_reclaim else 0) + (10 if higher_lows else 0)
    return clamp(score)


def score_dont_dilute_me(cash_ok=True, revenue_growth=True, rsi=50, dilution="Low"):
    score = 50 + (15 if cash_ok else -15) + (15 if revenue_growth else -10)
    score += 10 if 45 <= rsi <= 60 else -5
    score += 10 if dilution == "Low" else -15 if dilution == "High" else 0
    return clamp(score)


def score_early_explosion(tight=True, obv_up=True, rsi=55, macd_curl=True):
    score = 40 + (15 if tight else 0) + (15 if obv_up else 0) + (15 if 45 <= rsi <= 60 else 0) + (15 if macd_curl else 0)
    return clamp(score)
