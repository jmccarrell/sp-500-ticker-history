import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2013 = 499


def test_jan1_2013_count() -> None:
    assert len(sp500_tickers_as_of(2013, 1, 1)) == num_tickers_2013


def test_year_boundary_2013_2014() -> None:
    _test_at_year_boundary(2014)


def test_jan_2013_abbv_fii_swap() -> None:
    # Jan 2: AbbVie (ABBV) replaced Federated Investors (FII) after Abbott spinoff
    _test_one_swap(datetime.date.fromisoformat("2013-01-02"), "FII", "ABBV", num_tickers_2013)


def test_feb_2013_pvh_big_swap() -> None:
    # Feb 15: PVH (PVH) replaced Big Lots (BIG)
    _test_one_swap(datetime.date.fromisoformat("2013-02-15"), "BIG", "PVH", num_tickers_2013)


def test_apr_2013_regn_pcs_swap() -> None:
    # Apr 30: Regeneron (REGN) replaced MetroPCS (PCS) after T-Mobile acquisition
    _test_one_swap(datetime.date.fromisoformat("2013-04-30"), "PCS", "REGN", num_tickers_2013)


def test_may_2013_mac_cvh_swap() -> None:
    # May 8: Macerich (MAC) replaced Coventry Health Care (CVH) after Aetna acquisition
    _test_one_swap(datetime.date.fromisoformat("2013-05-08"), "CVH", "MAC", num_tickers_2013)


def test_may_2013_ksu_df_swap() -> None:
    # May 23: Kansas City Southern (KSU) replaced Dean Foods (DF)
    _test_one_swap(datetime.date.fromisoformat("2013-05-23"), "DF", "KSU", num_tickers_2013)


def test_jun_2013_gm_hnz_swap() -> None:
    # Jun 6: General Motors (GM) replaced Heinz (HNZ) after consortium acquisition
    _test_one_swap(datetime.date.fromisoformat("2013-06-06"), "HNZ", "GM", num_tickers_2013)


def test_jun_2013_zts_fhn_swap() -> None:
    # Jun 21: Zoetis (ZTS) replaced First Horizon (FHN) after Pfizer spinoff
    _test_one_swap(datetime.date.fromisoformat("2013-06-21"), "FHN", "ZTS", num_tickers_2013)


def test_jul_2013_nwsa_apol_swap() -> None:
    # Jul 1: News Corporation (NWSA) replaced Apollo Education Group (APOL)
    _test_one_swap(datetime.date.fromisoformat("2013-07-01"), "APOL", "NWSA", num_tickers_2013)


def test_jul_2013_nlsn_s_swap() -> None:
    # Jul 8: Nielsen (NLSN) replaced Sprint Nextel (S) after Softbank acquisition
    _test_one_swap(datetime.date.fromisoformat("2013-07-08"), "S", "NLSN", num_tickers_2013)


def test_sep_2013_dal_bmc_swap() -> None:
    # Sep 10: Delta Air Lines (DAL) replaced BMC Software (BMC) after going private
    _test_one_swap(datetime.date.fromisoformat("2013-09-10"), "BMC", "DAL", num_tickers_2013)


def test_sep_2013_bulk_swap() -> None:
    # Sep 20: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2013, 9, 19)
    tickers_after = sp500_tickers_as_of(2013, 9, 20)

    assert len(tickers_before) == num_tickers_2013
    assert len(tickers_after) == num_tickers_2013

    removed = {"AMD", "SAI"}
    added = {"AME", "VRTX"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2013_rig_dell_swap() -> None:
    # Oct 29: Transocean (RIG) replaced Dell (DELL) after going private
    _test_one_swap(datetime.date.fromisoformat("2013-10-29"), "DELL", "RIG", num_tickers_2013)


def test_nov_2013_cpri_nyx_swap() -> None:
    # Nov 13: Michael Kors/Capri Holdings (CPRI) replaced NYSE Euronext (NYX) after ICE acquisition
    _test_one_swap(datetime.date.fromisoformat("2013-11-13"), "NYX", "CPRI", num_tickers_2013)


def test_dec_2013_alle_jcp_swap() -> None:
    # Dec 2: Allegion (ALLE) replaced JCPenney (JCP) after Ingersoll Rand spinoff
    _test_one_swap(datetime.date.fromisoformat("2013-12-02"), "JCP", "ALLE", num_tickers_2013)


def test_dec_2013_ggp_molx_swap() -> None:
    # Dec 10: General Growth Properties (GGP) replaced Molex (MOLX) after Koch acquisition
    _test_one_swap(datetime.date.fromisoformat("2013-12-10"), "MOLX", "GGP", num_tickers_2013)


def test_dec_2013_bulk_swap() -> None:
    # Dec 23: 3-for-3 swap
    tickers_before = sp500_tickers_as_of(2013, 12, 22)
    tickers_after = sp500_tickers_as_of(2013, 12, 23)

    assert len(tickers_before) == num_tickers_2013
    assert len(tickers_after) == num_tickers_2013

    removed = {"ANF", "JDSU", "TER"}
    added = {"ADS", "META", "MHK"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
