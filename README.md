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

January 1, 2010 through at least February 9, 2026.

## Data Sources

This data is derived on a best-effort basis from the Wikipedia page
[List of S&P 500 companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies),
specifically the "Selected changes to the list of S&P 500 components" table.
It is **not** an authoritative or definitive source. The official S&P 500 index
composition is maintained by [S&P Dow Jones Indices](https://www.spglobal.com/spdji/).

Ticker symbols used throughout are the **current** trading symbols, even for
historical dates when a company may have traded under a different symbol.

## Depends on

The only truly required dependency is `uv`.
Optional, but almost always desirable:

- just
- direnv

## Show the recipes available

```text
just
```
