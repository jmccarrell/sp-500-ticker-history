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


def test_mar_2026_bulk_swap() -> None:
    # On Mar 23, 4-for-4 swap: COHR, LITE, ECHO, VRT replaced LW, MOH, MTCH, PAYC
    tickers_before = sp500_tickers_as_of(2026, 3, 22)
    tickers_after = sp500_tickers_as_of(2026, 3, 23)

    assert len(tickers_before) == num_tickers_2026
    assert len(tickers_after) == num_tickers_2026

    removed = {"LW", "MOH", "MTCH", "PAYC"}
    added = {"COHR", "ECHO", "LITE", "VRT"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_apr_2026_casy_holx_swap() -> None:
    # On Apr 9, Casey's (CASY) replaced Hologic (HOLX), taken private by Blackstone and TPG
    _test_one_swap(datetime.date.fromisoformat("2026-04-09"), "HOLX", "CASY", num_tickers_2026)


def test_may_2026_veev_ctra_swap() -> None:
    # On May 7, Veeva Systems (VEEV) replaced Coterra Energy (CTRA), acquired by Devon Energy
    _test_one_swap(datetime.date.fromisoformat("2026-05-07"), "CTRA", "VEEV", num_tickers_2026)


def test_jun_2026_fedex_freight_spinoff() -> None:
    # Jun 1: FedEx Freight (FDXF) spun off and added; the offsetting removal of EPAM lands Jun 2,
    # so the index holds 504 for one day
    assert len(sp500_tickers_as_of(2026, 5, 31)) == num_tickers_2026

    tickers_after_add = sp500_tickers_as_of(2026, 6, 1)
    assert len(tickers_after_add) == num_tickers_2026 + 1
    assert "FDXF" in tickers_after_add
    assert "EPAM" in tickers_after_add

    tickers_after_removal = sp500_tickers_as_of(2026, 6, 2)
    assert len(tickers_after_removal) == num_tickers_2026
    assert "EPAM" not in tickers_after_removal


def test_jun_2026_bulk_swap() -> None:
    # On Jun 22, 2-for-2 swap: FLEX, MRVL replaced CPB, POOL
    tickers_before = sp500_tickers_as_of(2026, 6, 21)
    tickers_after = sp500_tickers_as_of(2026, 6, 22)

    assert len(tickers_before) == num_tickers_2026
    assert len(tickers_after) == num_tickers_2026

    removed = {"CPB", "POOL"}
    added = {"FLEX", "MRVL"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_jun_2026_honeywell_aerospace_spinoff() -> None:
    # Jun 29: Honeywell Aerospace (HONA) spun off and added; the offsetting removal of CAG lands
    # Jun 30, so the index holds 504 for one day
    tickers_after_add = sp500_tickers_as_of(2026, 6, 29)
    assert len(tickers_after_add) == num_tickers_2026 + 1
    assert "HONA" in tickers_after_add
    assert "CAG" in tickers_after_add

    tickers_after_removal = sp500_tickers_as_of(2026, 6, 30)
    assert len(tickers_after_removal) == num_tickers_2026
    assert "CAG" not in tickers_after_removal


def test_aug_2026_ferg_ea_swap() -> None:
    # On Aug 5, Ferguson (FERG) replaced Electronic Arts (EA), taken private by a consortium led
    # by Saudi Arabia's Public Investment Fund
    _test_one_swap(datetime.date.fromisoformat("2026-08-05"), "EA", "FERG", num_tickers_2026)


def test_aug_2026_rddt_avb_swap() -> None:
    # On Aug 18, Reddit (RDDT) replaced AvalonBay Communities (AVB), acquired by Equity
    # Residential, which renamed itself Vivmark Residential (VMRK)
    _test_one_swap(datetime.date.fromisoformat("2026-08-18"), "AVB", "RDDT", num_tickers_2026)
