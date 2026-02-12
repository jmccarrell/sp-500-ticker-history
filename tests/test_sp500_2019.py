import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2019 = 505


def test_jan1_2019_count() -> None:
    assert len(sp500_tickers_as_of(2019, 1, 1)) == num_tickers_2019


def test_year_boundary_2019_2020() -> None:
    _test_at_year_boundary(2020)


def test_jan_2019_frc_scg_swap() -> None:
    # Jan 2: First Republic Bank (FRC) replaced SCANA (SCG) after Dominion Energy acquisition
    _test_one_swap(datetime.date.fromisoformat("2019-01-02"), "SCG", "FRC", num_tickers_2019)


def test_jan_2019_tfx_pcg_swap() -> None:
    # Jan 18: Teleflex (TFX) replaced Pacific Gas & Electric (PCG) after bankruptcy filing
    _test_one_swap(datetime.date.fromisoformat("2019-01-18"), "PCG", "TFX", num_tickers_2019)


def test_feb_2019_wab_gt_swap() -> None:
    # Feb 27: Wabtec (WAB) replaced Goodyear (GT) after GE transportation acquisition
    _test_one_swap(datetime.date.fromisoformat("2019-02-27"), "GT", "WAB", num_tickers_2019)


def test_apr_2019_dow_bhf_swap() -> None:
    # Apr 2: Dow (DOW) spun off from DowDuPont, replaced Brighthouse Financial (BHF)
    _test_one_swap(datetime.date.fromisoformat("2019-04-02"), "BHF", "DOW", num_tickers_2019)


def test_jun_2019_dwdp_spinoffs() -> None:
    # Jun 3: DowDuPont (DWDP) changed to DuPont (DD); Corteva (CTVA) spun off, replacing Fluor (FLR)
    tickers_before = sp500_tickers_as_of(2019, 6, 2)
    tickers_after = sp500_tickers_as_of(2019, 6, 3)

    assert len(tickers_before) == num_tickers_2019
    assert len(tickers_after) == num_tickers_2019

    removed = {"DWDP", "FLR"}
    added = {"DD", "CTVA"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_jun_2019_bemis_amcor_sequence() -> None:
    # Jun 7: Bemis (BMS) replaced Mattel (MAT) pending Amcor merger
    # Jun 11: Amcor (AMCR) replaced Bemis (BMS) after merger completed
    tickers_jun6 = sp500_tickers_as_of(2019, 6, 6)
    tickers_jun7 = sp500_tickers_as_of(2019, 6, 7)
    tickers_jun11 = sp500_tickers_as_of(2019, 6, 11)

    assert len(tickers_jun6) == num_tickers_2019
    assert len(tickers_jun7) == num_tickers_2019
    assert len(tickers_jun11) == num_tickers_2019

    assert "MAT" in tickers_jun6
    assert "BMS" not in tickers_jun6
    assert "AMCR" not in tickers_jun6

    assert "MAT" not in tickers_jun7
    assert "BMS" in tickers_jun7
    assert "AMCR" not in tickers_jun7

    assert "MAT" not in tickers_jun11
    assert "BMS" not in tickers_jun11
    assert "AMCR" in tickers_jun11


def test_jul_2019_mktx_lll_swap() -> None:
    # Jul 1: MarketAxess (MKTX) replaced L3 Technologies (LLL) after Harris acquisition
    _test_one_swap(datetime.date.fromisoformat("2019-07-01"), "LLL", "MKTX", num_tickers_2019)


def test_jul_2019_tmus_rht_swap() -> None:
    # Jul 15: T-Mobile (TMUS) replaced Red Hat (RHT) after IBM acquisition
    _test_one_swap(datetime.date.fromisoformat("2019-07-15"), "RHT", "TMUS", num_tickers_2019)


def test_aug_2019_bulk_swap() -> None:
    # Aug 9: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2019, 8, 8)
    tickers_after = sp500_tickers_as_of(2019, 8, 9)

    assert len(tickers_before) == num_tickers_2019
    assert len(tickers_after) == num_tickers_2019

    removed = {"APC", "FL"}
    added = {"LDOS", "IEX"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_sep_2019_cdw_tss_swap() -> None:
    # Sep 23: CDW (CDW) replaced TSYS (TSS) after Global Payments acquisition
    _test_one_swap(datetime.date.fromisoformat("2019-09-23"), "TSS", "CDW", num_tickers_2019)


def test_sep_2019_nvr_jef_swap() -> None:
    # Sep 26: NVR (NVR) replaced Jefferies (JEF)
    _test_one_swap(datetime.date.fromisoformat("2019-09-26"), "JEF", "NVR", num_tickers_2019)


def test_oct_2019_lvs_nktr_swap() -> None:
    # Oct 3: Las Vegas Sands (LVS) replaced Nektar Therapeutics (NKTR)
    _test_one_swap(datetime.date.fromisoformat("2019-10-03"), "NKTR", "LVS", num_tickers_2019)


def test_nov_2019_now_celg_swap() -> None:
    # Nov 21: ServiceNow (NOW) replaced Celgene (CELG) after Bristol-Myers Squibb acquisition
    _test_one_swap(datetime.date.fromisoformat("2019-11-21"), "CELG", "NOW", num_tickers_2019)


def test_dec_2019_wrb_viab_swap() -> None:
    # Dec 5: W. R. Berkley (WRB) replaced Viacom (VIAB) after CBS/Viacom merger
    _test_one_swap(datetime.date.fromisoformat("2019-12-05"), "VIAB", "WRB", num_tickers_2019)


def test_dec_2019_odfl_sti_swap() -> None:
    # Dec 9: Old Dominion Freight Line (ODFL) replaced SunTrust Banks (STI) after BB&T/Truist merger
    _test_one_swap(datetime.date.fromisoformat("2019-12-09"), "STI", "ODFL", num_tickers_2019)


def test_dec_2019_rebalance() -> None:
    # Dec 23: 3-for-3 rebalance
    tickers_before = sp500_tickers_as_of(2019, 12, 22)
    tickers_after = sp500_tickers_as_of(2019, 12, 23)

    assert len(tickers_before) == num_tickers_2019
    assert len(tickers_after) == num_tickers_2019

    removed = {"AMG", "MAC", "TRIP"}
    added = {"LYV", "STE", "ZBRA"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
