import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2021 = 505


def test_jan1_2021_count() -> None:
    assert len(sp500_tickers_as_of(2021, 1, 1)) == num_tickers_2021


def test_year_boundary_2021_2022() -> None:
    _test_at_year_boundary(2022)


def test_jan_2021_enph_tif_swap() -> None:
    # Jan 7: Enphase Energy (ENPH) replaced Tiffany (TIF) after LVMH acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-01-07"), "TIF", "ENPH", num_tickers_2021)


def test_jan_2021_trmb_cxo_swap() -> None:
    # Jan 21: Trimble (TRMB) replaced Concho Resources (CXO) after ConocoPhillips acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-01-21"), "CXO", "TRMB", num_tickers_2021)


def test_feb_2021_mpwr_fti_swap() -> None:
    # Feb 12: Monolithic Power (MPWR) replaced TechnipFMC (FTI)
    _test_one_swap(datetime.date.fromisoformat("2021-02-12"), "FTI", "MPWR", num_tickers_2021)


def test_mar_2021_bulk_swap() -> None:
    # Mar 22: 4-for-4 swap
    tickers_before = sp500_tickers_as_of(2021, 3, 21)
    tickers_after = sp500_tickers_as_of(2021, 3, 22)

    assert len(tickers_before) == num_tickers_2021
    assert len(tickers_after) == num_tickers_2021

    removed = {"FLS", "SLG", "VNT", "XRX"}
    added = {"CZR", "GNRC", "NXPI", "PENN"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_apr_2021_ptc_var_swap() -> None:
    # Apr 20: PTC replaced Varian Medical Systems (VAR) after Siemens acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-04-20"), "VAR", "PTC", num_tickers_2021)


def test_may_2021_crl_flir_swap() -> None:
    # May 14: Charles River Labs (CRL) replaced FLIR Systems (FLIR) after Teledyne acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-05-14"), "FLIR", "CRL", num_tickers_2021)


def test_jun_2021_ogn_spinoff_and_hfc_removal() -> None:
    # Jun 3: Organon (OGN) spun off from Merck
    tickers_jun2 = sp500_tickers_as_of(2021, 6, 2)
    tickers_jun3 = sp500_tickers_as_of(2021, 6, 3)
    assert len(tickers_jun2) == num_tickers_2021
    assert len(tickers_jun3) == num_tickers_2021 + 1
    assert "OGN" not in tickers_jun2
    assert "OGN" in tickers_jun3

    # Jun 4: HollyFrontier (HFC) removed for market cap
    tickers_jun4 = sp500_tickers_as_of(2021, 6, 4)
    assert len(tickers_jun4) == num_tickers_2021
    assert "HFC" in tickers_jun3
    assert "HFC" not in tickers_jun4


def test_jul_2021_mrna_alxn_swap() -> None:
    # Jul 21: Moderna (MRNA) replaced Alexion (ALXN) after AstraZeneca acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-07-21"), "ALXN", "MRNA", num_tickers_2021)


def test_aug_2021_tech_mxim_swap() -> None:
    # Aug 30: Bio-Techne (TECH) replaced Maxim Integrated (MXIM) after Analog Devices acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-08-30"), "MXIM", "TECH", num_tickers_2021)


def test_sep_2021_bulk_swap() -> None:
    # Sep 20: 3-for-3 swap
    tickers_before = sp500_tickers_as_of(2021, 9, 19)
    tickers_after = sp500_tickers_as_of(2021, 9, 20)

    assert len(tickers_before) == num_tickers_2021
    assert len(tickers_after) == num_tickers_2021

    removed = {"NOV", "PRGO", "UNM"}
    added = {"BRO", "DAY", "MTCH"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_dec_2021_epam_ksu_swap() -> None:
    # Dec 14: EPAM Systems replaced Kansas City Southern (KSU) after Canadian Pacific acquisition
    _test_one_swap(datetime.date.fromisoformat("2021-12-14"), "KSU", "EPAM", num_tickers_2021)


def test_dec_2021_rebalance() -> None:
    # Dec 20: 3-for-3 rebalance
    tickers_before = sp500_tickers_as_of(2021, 12, 19)
    tickers_after = sp500_tickers_as_of(2021, 12, 20)

    assert len(tickers_before) == num_tickers_2021
    assert len(tickers_after) == num_tickers_2021

    removed = {"HBI", "LEG", "WU"}
    added = {"FDS", "SBNY", "SEDG"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
