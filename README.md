# sp-500-ticker-history

Date-centric access to S&P 500 index membership over time.

## Usage

```python
from sp_500_ticker_history import sp500_tickers_as_of

# Get tickers as of a specific date
tickers = sp500_tickers_as_of(2026, 1, 1)
assert len(tickers) == 503
assert "AAPL" in tickers
```

## Coverage

January 1, 2018 through at least February 9, 2026.

## Depends on

The only truly required dependency is `uv`.
Optional, but almost always desirable:

- just
- direnv

## Show the recipes available

```text
just
```
