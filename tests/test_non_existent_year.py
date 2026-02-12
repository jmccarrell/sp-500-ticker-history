import pytest

from sp_500_ticker_history import sp500_tickers_as_of


def test_non_existent_year_raises(year: int = 2060) -> None:
    """
    Ensure we report a useful exception when asked for data we cannot provide.
    """
    with pytest.raises(NotImplementedError, match=f"no S&P 500 tickers defined for {year}"):
        sp500_tickers_as_of(year, 1, 1)
