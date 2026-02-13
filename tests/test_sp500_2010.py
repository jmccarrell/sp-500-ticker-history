import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2010 = 500


def test_jan1_2010_count() -> None:
    assert len(sp500_tickers_as_of(2010, 1, 1)) == num_tickers_2010


def test_year_boundary_2010_2011() -> None:
    _test_at_year_boundary(2011)


def test_feb_2010_hp_rx_swap() -> None:
    # Feb 26: Helmerich & Payne (HP) replaced IMS Health (RX) after going private
    _test_one_swap(datetime.date.fromisoformat("2010-02-26"), "RX", "HP", num_tickers_2010)


def test_apr_2010_cern_bjs_swap() -> None:
    # Apr 29: Cerner (CERN) replaced BJ Services (BJS) after Baker Hughes acquisition
    _test_one_swap(datetime.date.fromisoformat("2010-04-29"), "BJS", "CERN", num_tickers_2010)


def test_jun_2010_kmx_xto_swap() -> None:
    # Jun 28: CarMax (KMX) replaced XTO Energy (XTO) after ExxonMobil acquisition
    _test_one_swap(datetime.date.fromisoformat("2010-06-28"), "XTO", "KMX", num_tickers_2010)


def test_jun_2010_qep_str_swap() -> None:
    # Jun 30: QEP Resources (QEP) replaced Questar (STR) after company split
    _test_one_swap(datetime.date.fromisoformat("2010-06-30"), "STR", "QEP", num_tickers_2010)


def test_jul_2010_cb_mil_swap() -> None:
    # Jul 14: Chubb (CB) replaced Millipore (MIL) after Merck KGaA acquisition
    _test_one_swap(datetime.date.fromisoformat("2010-07-14"), "MIL", "CB", num_tickers_2010)


def test_aug_2010_tyc_sii_swap() -> None:
    # Aug 26: Tyco International (TYC) replaced Smith International (SII) after Schlumberger acquisition
    _test_one_swap(datetime.date.fromisoformat("2010-08-26"), "SII", "TYC", num_tickers_2010)


def test_nov_2010_tt_ptv_swap() -> None:
    # Nov 17: Ingersoll-Rand/Trane Technologies (TT) replaced Pactiv (PTV) after Reynolds acquisition
    _test_one_swap(datetime.date.fromisoformat("2010-11-17"), "PTV", "TT", num_tickers_2010)


def test_dec_2010_bulk_swap() -> None:
    # Dec 17: 4-for-4 swap
    tickers_before = sp500_tickers_as_of(2010, 12, 16)
    tickers_after = sp500_tickers_as_of(2010, 12, 17)

    assert len(tickers_before) == num_tickers_2010
    assert len(tickers_after) == num_tickers_2010

    removed = {"EK", "KG", "NYT", "ODP"}
    added = {"CVC", "FFIV", "NFLX", "NFX"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
