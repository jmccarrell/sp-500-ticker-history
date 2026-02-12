import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2015 = 501


def test_jan1_2015_count() -> None:
    assert len(sp500_tickers_as_of(2015, 1, 1)) == num_tickers_2015


def test_year_boundary_2015_2016() -> None:
    _test_at_year_boundary(2016)


def test_jan_2015_bulk_swap() -> None:
    # Jan 27: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2015, 1, 26)
    tickers_after = sp500_tickers_as_of(2015, 1, 27)

    assert len(tickers_before) == num_tickers_2015
    assert len(tickers_after) == num_tickers_2015

    removed = {"COV", "SWY"}
    added = {"ENDP", "HCA"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_mar_2015_swks_petm_swap() -> None:
    # Mar 12: Skyworks (SWKS) replaced PetSmart (PETM) after private equity acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-03-12"), "PETM", "SWKS", num_tickers_2015)


def test_mar_2015_hsic_cfn_swap() -> None:
    # Mar 18: Henry Schein (HSIC) replaced Carefusion (CFN) after BD acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-03-18"), "CFN", "HSIC", num_tickers_2015)


def test_mar_2015_rebalance() -> None:
    # Mar 23: 4-for-3 swap (AGN stays: Actavis acquired old Allergan, renamed to Allergan)
    tickers_before = sp500_tickers_as_of(2015, 3, 22)
    tickers_after = sp500_tickers_as_of(2015, 3, 23)

    assert len(tickers_before) == num_tickers_2015
    assert len(tickers_after) == num_tickers_2015 + 1  # 502

    removed = {"AVP", "DNR", "NBR"}
    added = {"AAL", "EQIX", "HBI", "SLG"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after

    # AGN stays in both (Actavis renamed to Allergan, kept AGN ticker)
    assert "AGN" in tickers_before
    assert "AGN" in tickers_after


num_tickers_after_mar23 = num_tickers_2015 + 1  # 502


def test_apr_2015_o_win_swap() -> None:
    # Apr 7: Realty Income (O) replaced Windstream (WIN)
    _test_one_swap(datetime.date.fromisoformat("2015-04-07"), "WIN", "O", num_tickers_after_mar23)


def test_jun_2015_qrvo_lo_swap() -> None:
    # Jun 11: Qorvo (QRVO) replaced Lorillard (LO) after acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-06-11"), "LO", "QRVO", num_tickers_after_mar23)


def test_jul_2015_bulk_swap() -> None:
    # Jul 1: 2-for-2 swap
    tickers_before = sp500_tickers_as_of(2015, 6, 30)
    tickers_after = sp500_tickers_as_of(2015, 7, 1)

    assert len(tickers_before) == num_tickers_after_mar23
    assert len(tickers_after) == num_tickers_after_mar23

    removed = {"QEP", "TEG"}
    added = {"BXLT", "JBHT"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_jul_2015_cpgx_ati_swap() -> None:
    # Jul 2: Columbia Pipeline (CPGX) replaced Allegheny Technologies (ATI)
    _test_one_swap(datetime.date.fromisoformat("2015-07-02"), "ATI", "CPGX", num_tickers_after_mar23)


def test_jul_2015_khc_krft_swap() -> None:
    # Jul 6: Kraft Heinz (KHC) replaced Kraft Foods (KRFT) after Heinz merger
    _test_one_swap(datetime.date.fromisoformat("2015-07-06"), "KRFT", "KHC", num_tickers_after_mar23)


def test_jul_2015_aap_fdo_swap() -> None:
    # Jul 8: Advance Auto Parts (AAP) replaced Family Dollar (FDO) after acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-07-08"), "FDO", "AAP", num_tickers_after_mar23)


def test_jul_2015_pypl_ne_swap() -> None:
    # Jul 20: PayPal (PYPL) replaced Noble Corporation (NE) after eBay spinoff
    _test_one_swap(datetime.date.fromisoformat("2015-07-20"), "NE", "PYPL", num_tickers_after_mar23)


def test_jul_2015_sig_dtv_swap() -> None:
    # Jul 29: Signet Jewelers (SIG) replaced DirecTV (DTV) after AT&T acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-07-29"), "DTV", "SIG", num_tickers_after_mar23)


def test_aug_2015_atvi_pll_swap() -> None:
    # Aug 28: Activision Blizzard (ATVI) replaced Pall Corporation (PLL) after takeover
    _test_one_swap(datetime.date.fromisoformat("2015-08-28"), "PLL", "ATVI", num_tickers_after_mar23)


def test_sep_2015_ual_hsp_swap() -> None:
    # Sep 2: United Airlines (UAL) replaced Hospira (HSP) after takeover
    _test_one_swap(datetime.date.fromisoformat("2015-09-02"), "HSP", "UAL", num_tickers_after_mar23)


def test_sep_2015_share_class_additions() -> None:
    # Sep 18: Share class methodology change added CMCSK, FOX, NWS (no removals)
    tickers_sep17 = sp500_tickers_as_of(2015, 9, 17)
    tickers_sep18 = sp500_tickers_as_of(2015, 9, 18)
    assert len(tickers_sep17) == num_tickers_after_mar23
    assert len(tickers_sep18) == num_tickers_after_mar23 + 3  # 505

    for ticker in ("CMCSK", "FOX", "NWS"):
        assert ticker not in tickers_sep17
        assert ticker in tickers_sep18


num_tickers_after_sep18 = num_tickers_after_mar23 + 3  # 505


def test_oct_2015_vrsk_joy_swap() -> None:
    # Oct 7: Verisk Analytics (VRSK) replaced Joy Global (JOY)
    _test_one_swap(datetime.date.fromisoformat("2015-10-07"), "JOY", "VRSK", num_tickers_after_sep18)


def test_nov_2015_hpe_hcbk_swap() -> None:
    # Nov 2: Hewlett Packard Enterprise (HPE) replaced Hudson City Bancorp (HCBK)
    _test_one_swap(datetime.date.fromisoformat("2015-11-02"), "HCBK", "HPE", num_tickers_after_sep18)


def test_nov_2015_syf_gnw_swap() -> None:
    # Nov 18: Synchrony Financial (SYF) replaced Genworth Financial (GNW)
    _test_one_swap(datetime.date.fromisoformat("2015-11-18"), "GNW", "SYF", num_tickers_after_sep18)


def test_nov_2015_ilmn_sial_swap() -> None:
    # Nov 19: Illumina (ILMN) replaced Sigma-Aldrich (SIAL) after Merck KGaA acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-11-19"), "SIAL", "ILMN", num_tickers_after_sep18)


def test_dec_2015_csra_csc_swap() -> None:
    # Dec 1: CSRA (CSRA) replaced Computer Sciences Corporation (CSC) after spinoff
    _test_one_swap(datetime.date.fromisoformat("2015-12-01"), "CSC", "CSRA", num_tickers_after_sep18)


def test_dec_2015_cmcsk_removal() -> None:
    # Dec 15: CMCSK shares no longer listed (removal only, count goes from 505 to 504)
    tickers_dec14 = sp500_tickers_as_of(2015, 12, 14)
    tickers_dec15 = sp500_tickers_as_of(2015, 12, 15)
    assert len(tickers_dec14) == num_tickers_after_sep18
    assert len(tickers_dec15) == num_tickers_after_sep18 - 1  # 504
    assert "CMCSK" in tickers_dec14
    assert "CMCSK" not in tickers_dec15


num_tickers_after_dec15 = num_tickers_after_sep18 - 1  # 504


def test_dec_2015_chd_altr_swap() -> None:
    # Dec 29: Church & Dwight (CHD) replaced Altera (ALTR) after Intel acquisition
    _test_one_swap(datetime.date.fromisoformat("2015-12-29"), "ALTR", "CHD", num_tickers_after_dec15)
