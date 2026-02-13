import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2018 = 506


def test_jan1_2018_count() -> None:
    assert len(sp500_tickers_as_of(2018, 1, 1)) == num_tickers_2018


def test_year_boundary_2018_2019() -> None:
    _test_at_year_boundary(2019)


def test_jan_2018_hii_bcr_swap() -> None:
    # Jan 3: Huntington Ingalls (HII) replaced CR Bard (BCR) after Becton Dickinson acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-01-03"), "BCR", "HII", num_tickers_2018)


def test_mar_2018_ipgp_sni_swap() -> None:
    # Mar 7: IPG Photonics (IPGP) replaced Scripps Networks (SNI) after Discovery acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-03-07"), "SNI", "IPGP", num_tickers_2018)


def test_mar_2018_rebalance() -> None:
    # Mar 19: 3-for-3 rebalance
    tickers_before = sp500_tickers_as_of(2018, 3, 18)
    tickers_after = sp500_tickers_as_of(2018, 3, 19)

    assert len(tickers_before) == num_tickers_2018
    assert len(tickers_after) == num_tickers_2018

    removed = {"CHK", "PDCO", "SIG"}
    added = {"NKTR", "SIVB", "TTWO"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_apr_2018_msci_csra_swap() -> None:
    # Apr 4: MSCI replaced CSRA after General Dynamics acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-04-04"), "CSRA", "MSCI", num_tickers_2018)


def test_may_2018_abmd_wyn_swap() -> None:
    # May 31: Abiomed (ABMD) replaced Wyndham Worldwide (WYN) after spinoff
    _test_one_swap(datetime.date.fromisoformat("2018-05-31"), "WYN", "ABMD", num_tickers_2018)


def test_jun_2018_evrg_navi_swap() -> None:
    # Jun 5: Evergy (EVRG) replaced Navient (NAVI)
    _test_one_swap(datetime.date.fromisoformat("2018-06-05"), "NAVI", "EVRG", num_tickers_2018)


def test_jun_2018_twtr_mon_swap() -> None:
    # Jun 7: Twitter (TWTR) replaced Monsanto (MON) after Bayer acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-06-07"), "MON", "TWTR", num_tickers_2018)


def test_jun_2018_bulk_swap() -> None:
    # Jun 18: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2018, 6, 17)
    tickers_after = sp500_tickers_as_of(2018, 6, 18)

    assert len(tickers_before) == num_tickers_2018
    assert len(tickers_after) == num_tickers_2018

    removed = {"AYI", "RRC"}
    added = {"BR", "HFC"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_jun_2018_cpay_twx_swap() -> None:
    # Jun 20: FleetCor (CPAY) replaced Time Warner (TWX) after AT&T acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-06-20"), "TWX", "CPAY", num_tickers_2018)


def test_jul_2018_cprt_dps_swap() -> None:
    # Jul 2: Copart (CPRT) replaced Dr Pepper Snapple (DPS) after Keurig acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-07-02"), "DPS", "CPRT", num_tickers_2018)


def test_aug_2018_anet_ggp_swap() -> None:
    # Aug 28: Arista Networks (ANET) replaced GGP after Brookfield acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-08-28"), "GGP", "ANET", num_tickers_2018)


def test_sep_2018_wcg_xl_swap() -> None:
    # Sep 14: WellCare (WCG) replaced XL Group (XL) after Axa acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-09-14"), "XL", "WCG", num_tickers_2018)


def test_oct_2018_rol_andv_swap() -> None:
    # Oct 1: Rollins (ROL) replaced Andeavor (ANDV) after Marathon Petroleum acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-10-01"), "ANDV", "ROL", num_tickers_2018)


def test_oct_2018_ftnt_evhc_swap() -> None:
    # Oct 11: Fortinet (FTNT) replaced Envision Healthcare (EVHC) after KKR acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-10-11"), "EVHC", "FTNT", num_tickers_2018)


def test_nov_2018_keys_ca_swap() -> None:
    # Nov 6: Keysight (KEYS) replaced CA Technologies (CA) after Broadcom acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-11-06"), "CA", "KEYS", num_tickers_2018)


def test_nov_2018_jkhy_eqt_swap() -> None:
    # Nov 13: Jack Henry (JKHY) replaced EQT Corporation (EQT) after ETRN spinoff
    _test_one_swap(datetime.date.fromisoformat("2018-11-13"), "EQT", "JKHY", num_tickers_2018)


def test_dec_2018_bulk_swap() -> None:
    # Dec 3: 3-for-3 swap
    tickers_before = sp500_tickers_as_of(2018, 12, 2)
    tickers_after = sp500_tickers_as_of(2018, 12, 3)

    assert len(tickers_before) == num_tickers_2018
    assert len(tickers_after) == num_tickers_2018

    removed = {"AET", "COL", "SRCL"}
    added = {"FANG", "LW", "MXIM"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_dec_2018_ce_esrx_swap() -> None:
    # Dec 24: Celanese (CE) replaced Express Scripts (ESRX) after Cigna acquisition
    _test_one_swap(datetime.date.fromisoformat("2018-12-24"), "ESRX", "CE", num_tickers_2018)
