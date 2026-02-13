import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2011 = 500


def test_jan1_2011_count() -> None:
    assert len(sp500_tickers_as_of(2011, 1, 1)) == num_tickers_2011


def test_year_boundary_2011_2012() -> None:
    _test_at_year_boundary(2012)


def test_jan_2011_mmi_mdp_swap() -> None:
    # Jan 3: Motorola Mobility (MMI) replaced Meredith Corp (MDP) after Motorola spinoff
    _test_one_swap(datetime.date.fromisoformat("2011-01-03"), "MDP", "MMI", num_tickers_2011)


def test_feb_2011_joy_aye_swap() -> None:
    # Feb 25: Joy Global (JOY) replaced Allegheny Energy (AYE) after FirstEnergy acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-02-25"), "AYE", "JOY", num_tickers_2011)


def test_feb_2011_cov_mfe_swap() -> None:
    # Feb 28: Covidien (COV) replaced McAfee (MFE) after Intel acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-02-28"), "MFE", "COV", num_tickers_2011)


def test_mar_2011_ew_q_swap() -> None:
    # Mar 31: Edwards Lifesciences (EW) replaced Qwest Communications (Q) after CenturyLink acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-03-31"), "Q", "EW", num_tickers_2011)


def test_apr_2011_blk_genz_swap() -> None:
    # Apr 1: BlackRock (BLK) replaced Genzyme (GENZ) after Sanofi acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-04-01"), "GENZ", "BLK", num_tickers_2011)


def test_apr_2011_cmg_novl_swap() -> None:
    # Apr 27: Chipotle (CMG) replaced Novell (NOVL) after private equity acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-04-27"), "NOVL", "CMG", num_tickers_2011)


def test_jun_2011_anr_mee_swap() -> None:
    # Jun 1: Alpha Natural Resources (ANR) replaced Massey Energy (MEE) after acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-06-01"), "MEE", "ANR", num_tickers_2011)


def test_jun_2011_mpc_rsh_swap() -> None:
    # Jun 30: Marathon Petroleum (MPC) replaced RadioShack (RSH)
    _test_one_swap(datetime.date.fromisoformat("2011-06-30"), "RSH", "MPC", num_tickers_2011)


def test_jul_2011_acn_mi_swap() -> None:
    # Jul 5: Accenture (ACN) replaced Marshall & Ilsley (MI) after Bank of Montreal acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-07-05"), "MI", "ACN", num_tickers_2011)


def test_sep_2011_mos_nsm_swap() -> None:
    # Sep 23: Mosaic Company (MOS) replaced National Semiconductor (NSM) after TI acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-09-23"), "NSM", "MOS", num_tickers_2011)


def test_oct_2011_tel_ceph_swap() -> None:
    # Oct 14: TE Connectivity (TEL) replaced Cephalon (CEPH) after Teva acquisition
    _test_one_swap(datetime.date.fromisoformat("2011-10-14"), "CEPH", "TEL", num_tickers_2011)


def test_oct_2011_xyl_itt_swap() -> None:
    # Oct 31: Xylem (XYL) replaced ITT (ITT) after ITT Corp spinoff
    _test_one_swap(datetime.date.fromisoformat("2011-10-31"), "ITT", "XYL", num_tickers_2011)


def test_nov_2011_cbe_jns_swap() -> None:
    # Nov 18: Cooper Industries (CBE) replaced Janus Capital Group (JNS)
    _test_one_swap(datetime.date.fromisoformat("2011-11-18"), "JNS", "CBE", num_tickers_2011)


def test_dec_2011_bulk_swap() -> None:
    # Dec 16: 3-for-3 swap
    tickers_before = sp500_tickers_as_of(2011, 12, 15)
    tickers_after = sp500_tickers_as_of(2011, 12, 16)

    assert len(tickers_before) == num_tickers_2011
    assert len(tickers_after) == num_tickers_2011

    removed = {"AKS", "MWW", "WFR"}
    added = {"BWA", "DLTR", "PRGO"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_dec_2011_trip_tlab_swap() -> None:
    # Dec 20: TripAdvisor (TRIP) replaced Tellabs (TLAB) after Expedia spinoff
    _test_one_swap(datetime.date.fromisoformat("2011-12-20"), "TLAB", "TRIP", num_tickers_2011)


def test_dec_2011_wpx_cpwr_swap() -> None:
    # Dec 31: WPX Energy (WPX) replaced Compuware (CPWR)
    _test_one_swap(datetime.date.fromisoformat("2011-12-31"), "CPWR", "WPX", num_tickers_2011)
