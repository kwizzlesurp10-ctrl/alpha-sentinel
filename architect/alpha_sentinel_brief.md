**AGENT BRIEF v0.1**
**Name**: Alpha Sentinel
**Domain/Niche**: Crypto Trading / Volatility Monitoring
**Objective & Success Metrics**: Deliver actionable, real-time alerts on market volatility and anomalous sentiment shifts. Success = actionable alerts with <30s latency.
**Target Deployment**: Telegram Bot (user-facing) + FastAPI/Background worker (data ingestion)

**Architect Output**:
- **Agent Design Canvas (7 sections)**:
    1. Mission: Alert users to volatility/sentiment spikes in real-time. Metric: Alert latency.
    2. Persona: Analytical, concise, objective "Market Sentinel".
    3. Knowledge: CoinGecko API (price), Twitter/X/Reddit (sentiment - scoped), VIX index proxy (if available).
- Capabilities: FetchPrice, AnalyzeSentiment, ThresholdCheck, SendAlert, SelfReflectAndPatch.
- State & Workflow: [Data Fetch] -> [Normalization] -> [Anomaly Detection] -> [Alert Logic] -> [Output] -> [Reflection Loop (Periodic)]
- Meta-Data: 
    - Created by: kwizzlesurp10-ctrl
    - Source Repository: https://github.com/kwizzlesurp10-ctrl/alpha-sentinel
    - Signature: [kwizzlesurp10-ctrl-signed-v0.1]
    - Self-Evolution: Periodic analysis of alert accuracy/utility leads to automatic updates of system_instructions.md.
    6. Guardrails: No trading execution (yet), rate-limiting for APIs, graceful failure on data source outage.
    7. Deployment: Dockerized service on Railway/Render.
- Tool Definitions: Need custom fetcher for price, sentiment aggregator.
- State Strategy: In-memory store (Redis later for persistence).

**Engineer Implementation Plan**:
- Structure: `/alpha-sentinel/engineer/` containing `main.py`, `bot.py`, `config.yaml`, `requirements.txt`.
- Libraries: `python-telegram-bot`, `httpx`, `pandas`, `sentiment-analysis-lib`.
- Integration: Telegram Bot is being integrated with `main.py` ingestion loop to provide real-time alerts.
- Build Order: 1. Setup API client. 2. Build data ingestion loop. 3. Build anomaly detection logic. 4. Integrate Telegram bot (In Progress). 5. Meta-Reflection loop deployed and operational.
- Test Strategy: Integration testing on testnet/sandbox API data.

**Reviewer Checklist**:
- [ ] Functionality: Does it fetch live?
- [ ] Reliability: Does it handle API errors?
- [ ] Fidelity: Does it match the Canvas?
- [ ] Safety: No trading keys needed (read-only).
- [ ] Performance: <1s per data fetch loop.

**Status**: DRAFT
**Feedback Loop**: Needs finalization of sentiment sources and thresholds.
