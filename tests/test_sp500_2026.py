import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2026 = 503


def test_year_boundary_2025_2026() -> None:
    assert len(sp500_tickers_as_of(2026, 1, 1)) == num_tickers_2026
    _test_at_year_boundary(2026)


def test_feb_2026_cien_day_swap() -> None:
    # On Feb 9, Ciena (CIEN) replaced Dayforce (DAY) after Thoma Bravo acquired Dayforce
    _test_one_swap(datetime.date.fromisoformat("2026-02-09"), "DAY", "CIEN", num_tickers_2026)
