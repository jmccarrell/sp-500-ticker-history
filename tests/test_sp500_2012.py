import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2012 = 500


def test_jan1_2012_count() -> None:
    assert len(sp500_tickers_as_of(2012, 1, 1)) == num_tickers_2012


def test_year_boundary_2012_2013() -> None:
    _test_at_year_boundary(2013)


def test_mar_2012_cci_ceg_swap() -> None:
    # Mar 13: Crown Castle (CCI) replaced Constellation Energy (CEG) after Exelon acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-03-13"), "CEG", "CCI", num_tickers_2012)


def test_apr_2012_fosl_mhs_swap() -> None:
    # Apr 3: Fossil (FOSL) replaced Medco Health Solutions (MHS) after Express Scripts acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-04-03"), "MHS", "FOSL", num_tickers_2012)


def test_apr_2012_psx_svu_swap() -> None:
    # Apr 23: Phillips 66 (PSX) replaced Supervalu (SVU) after ConocoPhillips spinoff
    _test_one_swap(datetime.date.fromisoformat("2012-04-23"), "SVU", "PSX", num_tickers_2012)


def test_may_2012_kmi_ep_swap() -> None:
    # May 17: Kinder Morgan (KMI) replaced El Paso Corporation (EP) after acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-05-17"), "EP", "KMI", num_tickers_2012)


def test_may_2012_alxn_mmi_swap() -> None:
    # May 21: Alexion (ALXN) replaced Motorola Mobility (MMI) after Google acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-05-21"), "MMI", "ALXN", num_tickers_2012)


def test_jun_2012_lrcx_nvls_swap() -> None:
    # Jun 5: Lam Research (LRCX) replaced Novellus Systems (NVLS) after acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-06-05"), "NVLS", "LRCX", num_tickers_2012)


def test_jun_2012_mnst_sle_swap() -> None:
    # Jun 29: Monster Beverage (MNST) replaced Sara Lee (SLE) after split up
    _test_one_swap(datetime.date.fromisoformat("2012-06-29"), "SLE", "MNST", num_tickers_2012)


def test_jul_2012_stx_pgn_swap() -> None:
    # Jul 2: Seagate Technology (STX) replaced Progress Energy (PGN) after Duke Energy acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-07-02"), "PGN", "STX", num_tickers_2012)


def test_jul_2012_esv_gr_swap() -> None:
    # Jul 31: Ensco (ESV) replaced Goodrich (GR) after United Technologies acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-07-31"), "GR", "ESV", num_tickers_2012)


def test_sep_2012_lyb_shld_swap() -> None:
    # Sep 5: LyondellBasell (LYB) replaced Sears Holdings (SHLD)
    _test_one_swap(datetime.date.fromisoformat("2012-09-05"), "SHLD", "LYB", num_tickers_2012)


def test_oct_2012_tyco_spinoff() -> None:
    # Oct 1: 2-for-2 swap from Tyco spinoffs
    tickers_before = sp500_tickers_as_of(2012, 9, 30)
    tickers_after = sp500_tickers_as_of(2012, 10, 1)

    assert len(tickers_before) == num_tickers_2012
    assert len(tickers_after) == num_tickers_2012

    removed = {"DV", "LXK"}
    added = {"ADT", "PNR"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2012_kraft_split() -> None:
    # Oct 2: Kraft Foods (KFT) renamed to Mondelez (MDLZ), new Kraft Foods Group (KRFT) split off
    tickers_before = sp500_tickers_as_of(2012, 10, 1)
    tickers_after = sp500_tickers_as_of(2012, 10, 2)

    assert len(tickers_before) == num_tickers_2012
    assert len(tickers_after) == num_tickers_2012

    removed = {"ANR", "KFT"}
    added = {"KRFT", "MDLZ"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2012_petm_sun_swap() -> None:
    # Oct 10: PetSmart (PETM) replaced Sunoco (SUN) after Energy Transfer Partners acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-10-10"), "SUN", "PETM", num_tickers_2012)


def test_dec_2012_dg_cbe_swap() -> None:
    # Dec 3: Dollar General (DG) replaced Cooper Industries (CBE) after Eaton acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-12-03"), "CBE", "DG", num_tickers_2012)


def test_dec_2012_grmn_rrd_swap() -> None:
    # Dec 11: Garmin (GRMN) replaced RR Donnelley (RRD)
    _test_one_swap(datetime.date.fromisoformat("2012-12-11"), "RRD", "GRMN", num_tickers_2012)


def test_dec_2012_aptv_tie_swap() -> None:
    # Dec 21: Delphi Automotive/Aptiv (APTV) replaced Titanium Metals (TIE) after PCP acquisition
    _test_one_swap(datetime.date.fromisoformat("2012-12-21"), "TIE", "APTV", num_tickers_2012)
