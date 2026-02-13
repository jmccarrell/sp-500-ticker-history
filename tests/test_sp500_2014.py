import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2014 = 500


def test_jan1_2014_count() -> None:
    assert len(sp500_tickers_as_of(2014, 1, 1)) == num_tickers_2014


def test_year_boundary_2014_2015() -> None:
    _test_at_year_boundary(2015)


def test_jan_2014_tsco_life_swap() -> None:
    # Jan 24: Tractor Supply (TSCO) replaced Life Technologies (LIFE) after Thermo Fisher acquisition
    _test_one_swap(datetime.date.fromisoformat("2014-01-24"), "LIFE", "TSCO", num_tickers_2014)


def test_mar_2014_gmcr_wpx_swap() -> None:
    # Mar 21: Keurig Green Mountain (GMCR) replaced WPX Energy (WPX)
    _test_one_swap(datetime.date.fromisoformat("2014-03-21"), "WPX", "GMCR", num_tickers_2014)


def test_apr_2014_ess_clf_swap() -> None:
    # Apr 2: Essex Property Trust (ESS) replaced Cliffs Natural Resources (CLF)
    _test_one_swap(datetime.date.fromisoformat("2014-04-02"), "CLF", "ESS", num_tickers_2014)


def test_apr_2014_googl_addition() -> None:
    # Apr 3: Google Class C (GOOGL) added, no removal (count goes from 499 to 500)
    tickers_apr2 = sp500_tickers_as_of(2014, 4, 2)
    tickers_apr3 = sp500_tickers_as_of(2014, 4, 3)
    assert len(tickers_apr2) == num_tickers_2014
    assert len(tickers_apr3) == num_tickers_2014 + 1
    assert "GOOGL" not in tickers_apr2
    assert "GOOGL" in tickers_apr3


num_tickers_after_apr3 = num_tickers_2014 + 1  # 501


def test_may_2014_bulk_swap() -> None:
    # May 1: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2014, 4, 30)
    tickers_after = sp500_tickers_as_of(2014, 5, 1)

    assert len(tickers_before) == num_tickers_after_apr3
    assert len(tickers_after) == num_tickers_after_apr3

    removed = {"BEAM", "SLM"}
    added = {"NAVI", "UAA"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_may_2014_avgo_lsi_swap() -> None:
    # May 8: Avago Technologies (AVGO) replaced LSI Corporation (LSI) after acquisition
    _test_one_swap(datetime.date.fromisoformat("2014-05-08"), "LSI", "AVGO", num_tickers_after_apr3)


def test_jun_2014_xec_igt_swap() -> None:
    # Jun 20: Cimarex Energy (XEC) replaced International Game Technology (IGT)
    _test_one_swap(datetime.date.fromisoformat("2014-06-20"), "IGT", "XEC", num_tickers_after_apr3)


def test_jul_2014_amg_frx_swap() -> None:
    # Jul 1: Affiliated Managers Group (AMG) replaced Forest Laboratories (FRX) after Actavis acquisition
    _test_one_swap(datetime.date.fromisoformat("2014-07-01"), "FRX", "AMG", num_tickers_after_apr3)


def test_jul_2014_mlm_x_swap() -> None:
    # Jul 2: Martin Marietta (MLM) replaced United States Steel (X)
    _test_one_swap(datetime.date.fromisoformat("2014-07-02"), "X", "MLM", num_tickers_after_apr3)


def test_aug_2014_disck_addition() -> None:
    # Aug 6: Discovery Communications Class C (DISCK) added, no removal (count goes from 500 to 501)
    tickers_aug5 = sp500_tickers_as_of(2014, 8, 5)
    tickers_aug6 = sp500_tickers_as_of(2014, 8, 6)
    assert len(tickers_aug5) == num_tickers_after_apr3
    assert len(tickers_aug6) == num_tickers_after_apr3 + 1
    assert "DISCK" not in tickers_aug5
    assert "DISCK" in tickers_aug6


num_tickers_after_aug6 = num_tickers_after_apr3 + 1  # 502


def test_aug_2014_mnk_rdc_swap() -> None:
    # Aug 18: Mallinckrodt (MNK) replaced Rowan Companies (RDC)
    _test_one_swap(datetime.date.fromisoformat("2014-08-18"), "RDC", "MNK", num_tickers_after_aug6)


def test_sep_2014_bulk_swap() -> None:
    # Sep 20: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2014, 9, 19)
    tickers_after = sp500_tickers_as_of(2014, 9, 20)

    assert len(tickers_before) == num_tickers_after_aug6
    assert len(tickers_after) == num_tickers_after_aug6

    removed = {"BTU", "GHC"}
    added = {"UHS", "URI"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_nov_2014_lvlt_jbl_swap() -> None:
    # Nov 5: Level 3 Communications (LVLT) replaced Jabil Circuit (JBL)
    _test_one_swap(datetime.date.fromisoformat("2014-11-05"), "JBL", "LVLT", num_tickers_after_aug6)


def test_dec_2014_rcl_bms_swap() -> None:
    # Dec 5: Royal Caribbean Cruises (RCL) replaced Bemis Company (BMS)
    _test_one_swap(datetime.date.fromisoformat("2014-12-05"), "BMS", "RCL", num_tickers_after_aug6)
