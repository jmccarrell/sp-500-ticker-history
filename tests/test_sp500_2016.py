import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2016 = 504


def test_jan1_2016_count() -> None:
    assert len(sp500_tickers_as_of(2016, 1, 1)) == num_tickers_2016


def test_year_boundary_2016_2017() -> None:
    _test_at_year_boundary(2017)


def test_jan_2016_wtw_fosl_swap() -> None:
    # Jan 5: Willis Towers Watson (WTW) replaced Fossil Group (FOSL) after Willis/Towers Watson merger
    _test_one_swap(datetime.date.fromisoformat("2016-01-05"), "FOSL", "WTW", num_tickers_2016)


def test_jan_2016_exr_ace_swap() -> None:
    # Jan 19: Extra Space Storage (EXR) replaced Chubb/ACE after ACE Ltd acquired Chubb
    _test_one_swap(datetime.date.fromisoformat("2016-01-19"), "ACE", "EXR", num_tickers_2016)


def test_feb_2016_bulk_swap() -> None:
    # Feb 1: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2016, 1, 31)
    tickers_after = sp500_tickers_as_of(2016, 2, 1)

    assert len(tickers_before) == num_tickers_2016
    assert len(tickers_after) == num_tickers_2016

    removed = {"BRCM", "PCP"}
    added = {"CFG", "FRT"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_feb_2016_cxo_pcl_swap() -> None:
    # Feb 22: Concho Resources (CXO) replaced Plum Creek Timber (PCL)
    _test_one_swap(datetime.date.fromisoformat("2016-02-22"), "PCL", "CXO", num_tickers_2016)


def test_mar_2016_awk_cnx_swap() -> None:
    # Mar 4: American Water Works (AWK) replaced Consol Energy (CNX)
    _test_one_swap(datetime.date.fromisoformat("2016-03-04"), "CNX", "AWK", num_tickers_2016)


def test_mar_2016_udr_gmcr_swap() -> None:
    # Mar 7: UDR replaced Keurig Green Mountain (GMCR) after JAB acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-03-07"), "GMCR", "UDR", num_tickers_2016)


def test_mar_2016_bulk_swap() -> None:
    # Mar 30: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2016, 3, 29)
    tickers_after = sp500_tickers_as_of(2016, 3, 30)

    assert len(tickers_before) == num_tickers_2016
    assert len(tickers_after) == num_tickers_2016

    removed = {"ESV", "POM"}
    added = {"CNC", "HOLX"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_apr_2016_fl_cam_swap() -> None:
    # Apr 4: Foot Locker (FL) replaced Cameron International (CAM) after Schlumberger acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-04-04"), "CAM", "FL", num_tickers_2016)


def test_apr_2016_ua_class_c_addition() -> None:
    # Apr 8: Under Armour Class C (UA) added, no removal (count goes from 504 to 505)
    tickers_apr7 = sp500_tickers_as_of(2016, 4, 7)
    tickers_apr8 = sp500_tickers_as_of(2016, 4, 8)
    assert len(tickers_apr7) == num_tickers_2016
    assert len(tickers_apr8) == num_tickers_2016 + 1
    assert "UA" not in tickers_apr7
    assert "UA" in tickers_apr8


def test_apr_2016_ulta_thc_swap() -> None:
    # Apr 18: Ulta Beauty (ULTA) replaced Tenet Healthcare (THC)
    _test_one_swap(datetime.date.fromisoformat("2016-04-18"), "THC", "ULTA", num_tickers_2016 + 1)


def test_apr_2016_gpn_gme_swap() -> None:
    # Apr 25: Global Payments (GPN) replaced GameStop (GME)
    _test_one_swap(datetime.date.fromisoformat("2016-04-25"), "GME", "GPN", num_tickers_2016 + 1)


def test_may_2016_ayi_adt_swap() -> None:
    # May 3: Acuity Brands (AYI) replaced ADT after Apollo acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-05-03"), "ADT", "AYI", num_tickers_2016 + 1)


def test_may_2016_alk_sndk_swap() -> None:
    # May 13: Alaska Air Group (ALK) replaced SanDisk (SNDK) after WDC acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-05-13"), "SNDK", "ALK", num_tickers_2016 + 1)


def test_may_2016_dlr_twc_swap() -> None:
    # May 18: Digital Realty (DLR) replaced Time Warner Cable (TWC) after Charter acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-05-18"), "TWC", "DLR", num_tickers_2016 + 1)


def test_may_2016_lkq_arg_swap() -> None:
    # May 23: LKQ (LKQ) replaced Airgas (ARG) after Air Liquide acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-05-23"), "ARG", "LKQ", num_tickers_2016 + 1)


def test_may_2016_ajg_cce_swap() -> None:
    # May 31: Arthur J. Gallagher (AJG) replaced Coca-Cola Enterprises (CCE)
    _test_one_swap(datetime.date.fromisoformat("2016-05-31"), "CCE", "AJG", num_tickers_2016 + 1)


def test_jun_2016_tdg_bxlt_swap() -> None:
    # Jun 3: TransDigm (TDG) replaced Baxalta (BXLT) after Shire acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-06-03"), "BXLT", "TDG", num_tickers_2016 + 1)


def test_jun_2016_fbhs_cvc_swap() -> None:
    # Jun 22: Fortune Brands (FBHS) replaced Cablevision (CVC) after Altice acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-06-22"), "CVC", "FBHS", num_tickers_2016 + 1)


def test_jul_2016_bulk_swap() -> None:
    # Jul 1: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2016, 6, 30)
    tickers_after = sp500_tickers_as_of(2016, 7, 1)

    assert len(tickers_before) == num_tickers_2016 + 1
    assert len(tickers_after) == num_tickers_2016 + 1

    removed = {"GAS", "TE"}
    added = {"ALB", "LNT"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_jul_2016_ftv_cpgx_swap() -> None:
    # Jul 5: Fortive (FTV) replaced Columbia Pipeline (CPGX) after TransCanada acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-07-05"), "CPGX", "FTV", num_tickers_2016 + 1)


def test_sep_2016_mtd_tyc_swap() -> None:
    # Sep 6: Mettler Toledo (MTD) replaced Tyco (TYC) after JCI/Tyco merger
    _test_one_swap(datetime.date.fromisoformat("2016-09-06"), "TYC", "MTD", num_tickers_2016 + 1)


def test_sep_2016_chtr_emc_swap() -> None:
    # Sep 8: Charter Communications (CHTR) replaced EMC after Dell acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-09-08"), "EMC", "CHTR", num_tickers_2016 + 1)


def test_sep_2016_coo_hot_swap() -> None:
    # Sep 22: Cooper Companies (COO) replaced Starwood (HOT) after Marriott acquisition
    _test_one_swap(datetime.date.fromisoformat("2016-09-22"), "HOT", "COO", num_tickers_2016 + 1)


def test_sep_2016_coty_do_swap() -> None:
    # Sep 30: Coty (COTY) replaced Diamond Offshore (DO)
    _test_one_swap(datetime.date.fromisoformat("2016-09-30"), "DO", "COTY", num_tickers_2016 + 1)


def test_nov_2016_arnc_aa_swap() -> None:
    # Nov 1: Arconic (ARNC) replaced Alcoa (AA) after Alcoa separation
    _test_one_swap(datetime.date.fromisoformat("2016-11-01"), "AA", "ARNC", num_tickers_2016 + 1)


def test_dec_2016_bulk_swap() -> None:
    # Dec 2: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2016, 12, 1)
    tickers_after = sp500_tickers_as_of(2016, 12, 2)

    assert len(tickers_before) == num_tickers_2016 + 1
    assert len(tickers_after) == num_tickers_2016 + 1

    removed = {"LM", "OI"}
    added = {"EVHC", "MAA"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
