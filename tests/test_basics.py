from sp_500_ticker_history import sp500_tickers_as_of


def test_basics() -> None:
    assert "AAPL" in sp500_tickers_as_of(2026, 1, 1)
    assert len(sp500_tickers_as_of(2026, 1, 1)) == 503
