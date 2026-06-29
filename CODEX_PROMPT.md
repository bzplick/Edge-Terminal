# Codex Build Prompt: Edge Terminal

Build a clean, mobile-first trading dashboard called **Edge Terminal**.

## Goal
Create a deployable GitHub/Railway-ready app that combines three scanners:

1. **Don't Dilute Me Scanner**
   - Price: $3–$20
   - Market cap: roughly $500M–$5B
   - Cash > debt OR positive operating cash flow
   - Within ~35% of 52-week low
   - RSI 45–60 and turning up
   - Positive revenue growth
   - No recent ATM/offering filing in the last ~6 months
   - Prefer institutional accumulation and organic 20%+ reversal potential

2. **Panic Reversal Scanner**
   - Price: $0.05–$20
   - Intraday drop >20% or down 30–80% from recent high
   - Relative volume >5x, ideal >10x
   - Dollar volume >$5M/day
   - RSI under 30, then curling up
   - MACD histogram improving or positive
   - Higher lows forming after capitulation
   - VWAP reclaim flag
   - Flag dilution/reverse split/Nasdaq deficiency/bankruptcy risk
   - Output: entry zone, stop, target 1, target 2, max hold time, conviction score

3. **Early Explosion Scanner**
   - Tight consolidation near lows
   - Rising OBV/ADL
   - Volume dry-up followed by relative volume expansion
   - RSI 45–60 and rising
   - MACD curl before crossover
   - Price reclaiming EMA 9/20 and VWAP
   - Float/short-interest awareness

## App Requirements
- Mobile-first single-page dashboard
- No broken buttons; if an API is unavailable, show mock data clearly marked as demo data
- Tabs or cards for: Live Scanner, Watchlist, Trade Plans, Filing Risk, Settings
- Each ticker card should show: ticker, price, % change, volume/RVOL, scanner bucket, conviction score, risk score, dilution warning, entry/stop/targets, VWAP status, RSI/MACD status, and a plain-English explanation.

## Tech Stack
- Frontend: React + Vite + TypeScript
- Styling: Tailwind CSS
- Backend: FastAPI Python service
- Data: mock JSON fallback first, then adapters for Polygon/Finnhub/Alpha Vantage/SEC EDGAR
- Deployment: Railway-friendly

## Backend Endpoints
- `GET /api/scanners/all`
- `GET /api/scanners/dont-dilute-me`
- `GET /api/scanners/panic-reversal`
- `GET /api/scanners/early-explosion`
- `GET /api/ticker/{symbol}`
- `GET /api/filings/{symbol}`
- `GET /api/health`

## Scoring Engine
Implement:
- `score_dont_dilute_me()`
- `score_panic_reversal()`
- `score_early_explosion()`
- `build_trade_plan()`
- `flag_dilution_risk()`

Return 0–100 scores with reasons.

## Filing Risk Rules
High-risk flags:
- ATM registration
- S-1, F-1, 424B, prospectus supplement
- reverse split
- Nasdaq deficiency notice
- going concern warning
- bankruptcy/restructuring language
- recent large warrant exercise or convertible note

## Output
Create a complete repo with:
- `README.md`
- `package.json`
- `vite.config.ts`
- `src/App.tsx`
- `src/components/*`
- `src/lib/scoring.ts`
- `backend/main.py`
- `backend/scoring.py`
- `backend/mock_data.py`
- `requirements.txt`
- `Procfile`
- `.env.example`

## UI Style
Dark mode, clean trading-terminal feel, easy to read on iPhone. Use large cards, clear green/red risk labels, and avoid clutter.

## Important
This is not financial advice. Add a small disclaimer in the UI footer. Do not place real trades. Scanner/watchlist software only.
