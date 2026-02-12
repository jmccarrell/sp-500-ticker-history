import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2022 = 505


def test_jan1_2022_count() -> None:
    assert len(sp500_tickers_as_of(2022, 1, 1)) == num_tickers_2022


def test_year_boundary_2022_2023() -> None:
    _test_at_year_boundary(2023)


def test_feb_2022_ceg_spinoff_and_gps_removal() -> None:
    # Feb 2: Constellation Energy (CEG) spun off from Exelon
    tickers_feb1 = sp500_tickers_as_of(2022, 2, 1)
    tickers_feb2 = sp500_tickers_as_of(2022, 2, 2)
    assert len(tickers_feb1) == num_tickers_2022
    assert len(tickers_feb2) == num_tickers_2022 + 1
    assert "CEG" not in tickers_feb1
    assert "CEG" in tickers_feb2

    # Feb 3: Gap (GPS) removed for market cap
    tickers_feb3 = sp500_tickers_as_of(2022, 2, 3)
    assert len(tickers_feb3) == num_tickers_2022
    assert "GPS" in tickers_feb2
    assert "GPS" not in tickers_feb3


def test_feb_2022_ndsn_xlnx_swap() -> None:
    # Feb 15: Nordson (NDSN) replaced Xilinx (XLNX) after AMD acquisition
    _test_one_swap(datetime.date.fromisoformat("2022-02-15"), "XLNX", "NDSN", num_tickers_2022)


def test_mar_2022_moh_info_swap() -> None:
    # Mar 2: Molina Healthcare (MOH) replaced IHS Markit (INFO)
    _test_one_swap(datetime.date.fromisoformat("2022-03-02"), "INFO", "MOH", num_tickers_2022)


def test_apr_2022_cpt_pbct_swap() -> None:
    # Apr 4: Camden Property Trust (CPT) replaced People's United Financial (PBCT)
    _test_one_swap(datetime.date.fromisoformat("2022-04-04"), "PBCT", "CPT", num_tickers_2022)


def test_apr_2022_wbd_discovery_merger() -> None:
    # Apr 11: Warner Bros. Discovery (WBD) replaced both Discovery share classes (DISCA, DISCK)
    tickers_before = sp500_tickers_as_of(2022, 4, 10)
    tickers_after = sp500_tickers_as_of(2022, 4, 11)

    assert len(tickers_before) == num_tickers_2022
    assert len(tickers_after) == num_tickers_2022 - 1  # 2 removed, 1 added

    assert "DISCA" in tickers_before
    assert "DISCK" in tickers_before
    assert "DISCA" not in tickers_after
    assert "DISCK" not in tickers_after
    assert "WBD" not in tickers_before
    assert "WBD" in tickers_after


def test_jun_2022_vici_cern_swap() -> None:
    # Jun 8: Vici Properties (VICI) replaced Cerner (CERN) after Oracle acquisition
    _test_one_swap(datetime.date.fromisoformat("2022-06-08"), "CERN", "VICI", num_tickers_2022 - 1)


def test_jun_2022_under_armour_removal() -> None:
    # Jun 21: KDP and ON added; UA, UAA, IPGP removed (net -1)
    tickers_before = sp500_tickers_as_of(2022, 6, 20)
    tickers_after = sp500_tickers_as_of(2022, 6, 21)

    assert len(tickers_before) == num_tickers_2022 - 1  # after Apr 11 merger
    assert len(tickers_after) == num_tickers_2022 - 2  # net -1

    removed = {"IPGP", "UA", "UAA"}
    added = {"KDP", "ON"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_sep_2022_bulk_swap() -> None:
    # Sep 19: CoStar (CSGP) and Invitation Homes (INVH) replaced PVH and Penn Entertainment
    tickers_before = sp500_tickers_as_of(2022, 9, 18)
    tickers_after = sp500_tickers_as_of(2022, 9, 19)

    removed = {"PVH", "PENN"}
    added = {"CSGP", "INVH"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2022_bulk_swap() -> None:
    # Oct 3: PG&E (PCG) and EQT replaced Citrix (CTXS) and Duke Realty (DRE)
    tickers_before = sp500_tickers_as_of(2022, 10, 2)
    tickers_after = sp500_tickers_as_of(2022, 10, 3)

    removed = {"CTXS", "DRE"}
    added = {"EQT", "PCG"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2022_trgp_nlsn_swap() -> None:
    # Oct 12: Targa Resources (TRGP) replaced Nielsen (NLSN)
    _test_one_swap(datetime.date.fromisoformat("2022-10-12"), "NLSN", "TRGP", num_tickers_2022 - 2)


def test_nov_2022_acgl_twtr_swap() -> None:
    # Nov 1: Arch Capital (ACGL) replaced Twitter (TWTR) after Elon Musk acquisition
    _test_one_swap(datetime.date.fromisoformat("2022-11-01"), "TWTR", "ACGL", num_tickers_2022 - 2)


def test_dec_2022_mbc_spinoff_and_rebalance() -> None:
    # Dec 15: MasterBrand (MBC) spun off from Fortune Brands
    tickers_dec14 = sp500_tickers_as_of(2022, 12, 14)
    tickers_dec15 = sp500_tickers_as_of(2022, 12, 15)
    assert len(tickers_dec15) == len(tickers_dec14) + 1
    assert "MBC" not in tickers_dec14
    assert "MBC" in tickers_dec15

    # Dec 19: First Solar (FSLR) replaced Fortune Brands (FBHS) and MasterBrand (MBC)
    tickers_dec19 = sp500_tickers_as_of(2022, 12, 19)
    assert "FSLR" not in tickers_dec15
    assert "FSLR" in tickers_dec19
    assert "FBHS" in tickers_dec15
    assert "FBHS" not in tickers_dec19
    assert "MBC" not in tickers_dec19


def test_dec_2022_stld_abmd_swap() -> None:
    # Dec 22: Steel Dynamics (STLD) replaced Abiomed (ABMD) after J&J acquisition
    _test_one_swap(datetime.date.fromisoformat("2022-12-22"), "ABMD", "STLD", num_tickers_2022 - 2)
