import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2020 = 505


def test_jan1_2020_count() -> None:
    assert len(sp500_tickers_as_of(2020, 1, 1)) == num_tickers_2020


def test_year_boundary_2020_2021() -> None:
    _test_at_year_boundary(2021)


def test_jan_2020_payc_wcg_swap() -> None:
    # Jan 28: Paycom (PAYC) replaced WellCare (WCG) after Centene acquisition
    _test_one_swap(datetime.date.fromisoformat("2020-01-28"), "WCG", "PAYC", num_tickers_2020)


def test_mar_2020_ir_xec_swap() -> None:
    # Mar 2: Ingersoll Rand (IR) replaced Cimarex Energy (XEC)
    _test_one_swap(datetime.date.fromisoformat("2020-03-02"), "XEC", "IR", num_tickers_2020)


def test_apr_2020_hwm_arnc_swap() -> None:
    # Apr 1: Howmet Aerospace (HWM) replaced Arconic (ARNC) after company separation
    _test_one_swap(datetime.date.fromisoformat("2020-04-01"), "ARNC", "HWM", num_tickers_2020)


def test_apr_2020_utx_spinoffs_and_removals() -> None:
    # Apr 3: United Technologies spun off OTIS and CARR (count goes to 507)
    tickers_apr2 = sp500_tickers_as_of(2020, 4, 2)
    tickers_apr3 = sp500_tickers_as_of(2020, 4, 3)
    assert len(tickers_apr2) == num_tickers_2020
    assert len(tickers_apr3) == num_tickers_2020 + 2
    assert "OTIS" not in tickers_apr2
    assert "CARR" not in tickers_apr2
    assert "OTIS" in tickers_apr3
    assert "CARR" in tickers_apr3

    # Apr 6: M and RTN removed (count back to 505)
    tickers_apr6 = sp500_tickers_as_of(2020, 4, 6)
    assert len(tickers_apr6) == num_tickers_2020
    assert "M" in tickers_apr3
    assert "M" not in tickers_apr6
    assert "RTN" in tickers_apr3
    assert "RTN" not in tickers_apr6


def test_may_2020_bulk_swap() -> None:
    # May 12: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2020, 5, 11)
    tickers_after = sp500_tickers_as_of(2020, 5, 12)

    assert len(tickers_before) == num_tickers_2020
    assert len(tickers_after) == num_tickers_2020

    removed = {"AGN", "CPRI"}
    added = {"DPZ", "DXCM"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_may_2020_wst_hp_swap() -> None:
    # May 22: West Pharmaceutical (WST) replaced Helmerich & Payne (HP)
    _test_one_swap(datetime.date.fromisoformat("2020-05-22"), "HP", "WST", num_tickers_2020)


def test_jun_2020_bulk_swap() -> None:
    # Jun 22: 3-for-3 swap
    tickers_before = sp500_tickers_as_of(2020, 6, 21)
    tickers_after = sp500_tickers_as_of(2020, 6, 22)

    assert len(tickers_before) == num_tickers_2020
    assert len(tickers_after) == num_tickers_2020

    removed = {"ADS", "HOG", "JWN"}
    added = {"BIO", "TDY", "TYL"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_sep_2020_bulk_swap() -> None:
    # Sep 21: 3-for-3 swap
    tickers_before = sp500_tickers_as_of(2020, 9, 20)
    tickers_after = sp500_tickers_as_of(2020, 9, 21)

    assert len(tickers_before) == num_tickers_2020
    assert len(tickers_after) == num_tickers_2020

    removed = {"COTY", "HRB", "KSS"}
    added = {"CTLT", "ETSY", "TER"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2020_pool_etfc_swap() -> None:
    # Oct 7: Pool Corporation (POOL) replaced E-Trade (ETFC) after Morgan Stanley acquisition
    _test_one_swap(datetime.date.fromisoformat("2020-10-07"), "ETFC", "POOL", num_tickers_2020)


def test_oct_2020_vnt_spinoff_and_nbl_removal() -> None:
    # Oct 9: Vontier (VNT) spun off from Fortive
    tickers_oct8 = sp500_tickers_as_of(2020, 10, 8)
    tickers_oct9 = sp500_tickers_as_of(2020, 10, 9)
    assert len(tickers_oct8) == num_tickers_2020
    assert len(tickers_oct9) == num_tickers_2020 + 1
    assert "VNT" not in tickers_oct8
    assert "VNT" in tickers_oct9

    # Oct 12: Noble Energy (NBL) removed after Chevron acquisition
    tickers_oct12 = sp500_tickers_as_of(2020, 10, 12)
    assert len(tickers_oct12) == num_tickers_2020
    assert "NBL" in tickers_oct9
    assert "NBL" not in tickers_oct12


def test_dec_2020_tsla_aiv_swap() -> None:
    # Dec 21: Tesla (TSLA) replaced Apartment Investment & Management (AIV)
    _test_one_swap(datetime.date.fromisoformat("2020-12-21"), "AIV", "TSLA", num_tickers_2020)
