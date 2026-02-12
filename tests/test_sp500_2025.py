import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2025 = 503


def test_jan1_2025_count() -> None:
    assert len(sp500_tickers_as_of(2025, 1, 1)) == num_tickers_2025


def test_mar_2025_bulk_swap() -> None:
    # On Mar 24, 4-for-4 swap: DASH, EXE, TKO, WSM replaced BWA, CE, FMC, TFX
    tickers_before = sp500_tickers_as_of(2025, 3, 23)
    tickers_after = sp500_tickers_as_of(2025, 3, 24)

    assert len(tickers_before) == num_tickers_2025
    assert len(tickers_after) == num_tickers_2025

    removed = {"BWA", "CE", "FMC", "TFX"}
    added = {"DASH", "EXE", "TKO", "WSM"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_may_2025_coin_dfs_swap() -> None:
    # On May 19, Coinbase (COIN) replaced Discover Financial (DFS)
    _test_one_swap(datetime.date.fromisoformat("2025-05-19"), "DFS", "COIN", num_tickers_2025)


def test_jul_2025_ddog_jnpr_swap() -> None:
    # On Jul 9, Datadog (DDOG) replaced Juniper Networks (JNPR)
    _test_one_swap(datetime.date.fromisoformat("2025-07-09"), "JNPR", "DDOG", num_tickers_2025)


def test_jul_2025_ttd_anss_swap() -> None:
    # On Jul 18, The Trade Desk (TTD) replaced Ansys (ANSS)
    _test_one_swap(datetime.date.fromisoformat("2025-07-18"), "ANSS", "TTD", num_tickers_2025)


def test_jul_2025_xyz_hes_swap() -> None:
    # On Jul 23, Block (XYZ) replaced Hess (HES)
    _test_one_swap(datetime.date.fromisoformat("2025-07-23"), "HES", "XYZ", num_tickers_2025)


def test_aug_2025_ibkr_wba_swap() -> None:
    # On Aug 28, Interactive Brokers (IBKR) replaced Walgreens (WBA)
    _test_one_swap(datetime.date.fromisoformat("2025-08-28"), "WBA", "IBKR", num_tickers_2025)


def test_sep_2025_bulk_swap() -> None:
    # On Sep 22, 3-for-3 swap: APP, EME, HOOD replaced CZR, ENPH, MKTX
    tickers_before = sp500_tickers_as_of(2025, 9, 21)
    tickers_after = sp500_tickers_as_of(2025, 9, 22)

    assert len(tickers_before) == num_tickers_2025
    assert len(tickers_after) == num_tickers_2025

    removed = {"CZR", "ENPH", "MKTX"}
    added = {"APP", "EME", "HOOD"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2025_sols_added() -> None:
    # On Oct 30, Solstice Advanced Materials (SOLS) spun off from Honeywell
    tickers_before = sp500_tickers_as_of(2025, 10, 29)
    tickers_after = sp500_tickers_as_of(2025, 10, 30)
    assert len(tickers_before) == num_tickers_2025
    assert len(tickers_after) == num_tickers_2025 + 1
    assert "SOLS" not in tickers_before
    assert "SOLS" in tickers_after


def test_oct_2025_kmx_removed() -> None:
    # On Oct 31, CarMax (KMX) removed for market cap
    tickers_before = sp500_tickers_as_of(2025, 10, 30)
    tickers_after = sp500_tickers_as_of(2025, 10, 31)
    assert len(tickers_before) == num_tickers_2025 + 1
    assert len(tickers_after) == num_tickers_2025
    assert "KMX" in tickers_before
    assert "KMX" not in tickers_after


def test_nov_2025_q_added() -> None:
    # On Nov 3, Qnity Electronics (Q) spun off from DuPont
    tickers_before = sp500_tickers_as_of(2025, 11, 2)
    tickers_after = sp500_tickers_as_of(2025, 11, 3)
    assert len(tickers_before) == num_tickers_2025
    assert len(tickers_after) == num_tickers_2025 + 1
    assert "Q" not in tickers_before
    assert "Q" in tickers_after


def test_nov_2025_emn_removed() -> None:
    # On Nov 4, Eastman Chemical (EMN) removed for market cap
    tickers_before = sp500_tickers_as_of(2025, 11, 3)
    tickers_after = sp500_tickers_as_of(2025, 11, 4)
    assert len(tickers_before) == num_tickers_2025 + 1
    assert len(tickers_after) == num_tickers_2025
    assert "EMN" in tickers_before
    assert "EMN" not in tickers_after


def test_nov_2025_sndk_ipg_swap() -> None:
    # On Nov 28, Sandisk (SNDK) replaced Interpublic Group (IPG)
    _test_one_swap(datetime.date.fromisoformat("2025-11-28"), "IPG", "SNDK", num_tickers_2025)


def test_dec_2025_ares_k_swap() -> None:
    # On Dec 11, Ares Management (ARES) replaced Kellanova (K)
    _test_one_swap(datetime.date.fromisoformat("2025-12-11"), "K", "ARES", num_tickers_2025)


def test_dec_2025_rebalance() -> None:
    # On Dec 22, 3-for-3 rebalance: CRH, CVNA, FIX replaced LKQ, MHK, SOLS
    tickers_before = sp500_tickers_as_of(2025, 12, 21)
    tickers_after = sp500_tickers_as_of(2025, 12, 22)

    assert len(tickers_before) == num_tickers_2025
    assert len(tickers_after) == num_tickers_2025

    removed = {"LKQ", "MHK", "SOLS"}
    added = {"CRH", "CVNA", "FIX"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
