import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2017 = 505


def test_jan1_2017_count() -> None:
    assert len(sp500_tickers_as_of(2017, 1, 1)) == num_tickers_2017


def test_year_boundary_2017_2018() -> None:
    _test_at_year_boundary(2018)


def test_jan_2017_idxx_stj_swap() -> None:
    # Jan 5: IDEXX Labs (IDXX) replaced St. Jude Medical (STJ) after Abbott acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-01-05"), "STJ", "IDXX", num_tickers_2017)


def test_feb_2017_incy_se_swap() -> None:
    # Feb 28: Incyte (INCY) replaced Spectra Energy (SE) after Enbridge acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-02-28"), "SE", "INCY", num_tickers_2017)


def test_mar_2017_cboe_pbi_swap() -> None:
    # Mar 1: Cboe (CBOE) replaced Pitney Bowes (PBI) after BATS acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-03-01"), "PBI", "CBOE", num_tickers_2017)


def test_mar_2017_reg_endp_swap() -> None:
    # Mar 2: Regency Centers (REG) replaced Endo International (ENDP)
    _test_one_swap(datetime.date.fromisoformat("2017-03-02"), "ENDP", "REG", num_tickers_2017)


def test_mar_2017_dish_lltc_swap() -> None:
    # Mar 13: Dish Network (DISH) replaced Linear Technology (LLTC) after Analog Devices acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-03-13"), "LLTC", "DISH", num_tickers_2017)


def test_mar_2017_snps_har_swap() -> None:
    # Mar 16: Synopsys (SNPS) replaced Harman International (HAR) after Samsung acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-03-16"), "HAR", "SNPS", num_tickers_2017)


def test_mar_2017_rebalance() -> None:
    # Mar 20: 3-for-3 rebalance
    tickers_before = sp500_tickers_as_of(2017, 3, 19)
    tickers_after = sp500_tickers_as_of(2017, 3, 20)

    assert len(tickers_before) == num_tickers_2017
    assert len(tickers_after) == num_tickers_2017

    removed = {"FSLR", "FTR", "URBN"}
    added = {"AMD", "ARE", "RJF"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_apr_2017_dxc_swn_swap() -> None:
    # Apr 4: DXC Technology (DXC) replaced Southwestern Energy (SWN) after HPE/CSC merger
    _test_one_swap(datetime.date.fromisoformat("2017-04-04"), "SWN", "DXC", num_tickers_2017)


def test_apr_2017_it_dnb_swap() -> None:
    # Apr 5: Gartner (IT) replaced Dun & Bradstreet (DNB) after CEB acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-04-05"), "DNB", "IT", num_tickers_2017)


def test_jun_2017_info_tgna_swap() -> None:
    # Jun 2: IHS Markit (INFO) replaced Tegna (TGNA) after Cars.com spinoff
    _test_one_swap(datetime.date.fromisoformat("2017-06-02"), "TGNA", "INFO", num_tickers_2017)


def test_jun_2017_bulk_swap() -> None:
    # Jun 19: 4-for-4 swap
    tickers_before = sp500_tickers_as_of(2017, 6, 18)
    tickers_after = sp500_tickers_as_of(2017, 6, 19)

    assert len(tickers_before) == num_tickers_2017
    assert len(tickers_after) == num_tickers_2017

    removed = {"MJN", "R", "TDC", "YHOO"}
    added = {"ALGN", "ANSS", "EG", "HLT"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_jul_2017_bkr_bhi_swap() -> None:
    # Jul 7: Baker Hughes (BKR) replaced Baker Hughes (BHI) after GE Oil & Gas merger
    _test_one_swap(datetime.date.fromisoformat("2017-07-07"), "BHI", "BKR", num_tickers_2017)


def test_jul_2017_bulk_swap() -> None:
    # Jul 26: 5-for-5 swap
    tickers_before = sp500_tickers_as_of(2017, 7, 25)
    tickers_after = sp500_tickers_as_of(2017, 7, 26)

    assert len(tickers_before) == num_tickers_2017
    assert len(tickers_after) == num_tickers_2017

    removed = {"BBBY", "MNK", "MUR", "RAI", "RIG"}
    added = {"AOS", "DRE", "MGM", "PKG", "RMD"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_aug_2017_bhf_an_swap() -> None:
    # Aug 8: Brighthouse Financial (BHF) replaced AutoNation (AN) after MetLife spinoff
    _test_one_swap(datetime.date.fromisoformat("2017-08-08"), "AN", "BHF", num_tickers_2017)


def test_aug_2017_iqv_wfm_swap() -> None:
    # Aug 29: IQVIA (IQV) replaced Whole Foods (WFM) after Amazon acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-08-29"), "WFM", "IQV", num_tickers_2017)


def test_sep_2017_dowdupont_merger() -> None:
    # Sep 1: Dow Chemical (DOW) renamed to DowDuPont (DWDP) after acquiring DuPont (DD);
    #         SBA Communications (SBAC) replaced DuPont (DD)
    tickers_before = sp500_tickers_as_of(2017, 8, 31)
    tickers_after = sp500_tickers_as_of(2017, 9, 1)

    assert len(tickers_before) == num_tickers_2017
    assert len(tickers_after) == num_tickers_2017

    removed = {"DD", "DOW"}
    added = {"DWDP", "SBAC"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_sep_2017_cdns_spls_swap() -> None:
    # Sep 18: Cadence Design (CDNS) replaced Staples (SPLS) after Sycamore acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-09-18"), "SPLS", "CDNS", num_tickers_2017)


def test_oct_2017_nclh_lvlt_swap() -> None:
    # Oct 13: Norwegian Cruise Line (NCLH) replaced Level 3 (LVLT) after CenturyLink acquisition
    _test_one_swap(datetime.date.fromisoformat("2017-10-13"), "LVLT", "NCLH", num_tickers_2017)
