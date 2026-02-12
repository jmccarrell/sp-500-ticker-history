import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2024 = 503


def test_jan1_2024_count() -> None:
    assert len(sp500_tickers_as_of(2024, 1, 1)) == num_tickers_2024


def test_year_boundary_2024_2025() -> None:
    _test_at_year_boundary(2025)


def test_mar_2024_smci_deck_swap() -> None:
    # On Mar 18, Supermicro (SMCI) and Deckers (DECK) replaced Whirlpool (WHR) and Zions (ZION)
    tickers_before = sp500_tickers_as_of(2024, 3, 17)
    tickers_after = sp500_tickers_as_of(2024, 3, 18)

    assert len(tickers_before) == num_tickers_2024
    assert len(tickers_after) == num_tickers_2024

    removed = {"WHR", "ZION"}
    added = {"DECK", "SMCI"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_apr_2024_spinoffs_and_removals() -> None:
    # Apr 1: Solventum (SOLV) spun off from 3M
    tickers_mar31 = sp500_tickers_as_of(2024, 3, 31)
    tickers_apr1 = sp500_tickers_as_of(2024, 4, 1)
    assert len(tickers_apr1) == num_tickers_2024 + 1
    assert "SOLV" not in tickers_mar31
    assert "SOLV" in tickers_apr1

    # Apr 2: GE Vernova (GEV) spun off from GE
    tickers_apr2 = sp500_tickers_as_of(2024, 4, 2)
    assert len(tickers_apr2) == num_tickers_2024 + 2
    assert "GEV" not in tickers_apr1
    assert "GEV" in tickers_apr2

    # Apr 3: VFC and XRAY removed for market cap
    tickers_apr3 = sp500_tickers_as_of(2024, 4, 3)
    assert len(tickers_apr3) == num_tickers_2024
    assert "VFC" in tickers_apr2
    assert "XRAY" in tickers_apr2
    assert "VFC" not in tickers_apr3
    assert "XRAY" not in tickers_apr3


def test_may_2024_vst_pxd_swap() -> None:
    # On May 8, Vistra (VST) replaced Pioneer Natural Resources (PXD)
    _test_one_swap(datetime.date.fromisoformat("2024-05-08"), "PXD", "VST", num_tickers_2024)


def test_jun_2024_bulk_swap() -> None:
    # On Jun 24, 3-for-3: KKR, CrowdStrike, GoDaddy replaced RHI, Comerica, Illumina
    tickers_before = sp500_tickers_as_of(2024, 6, 23)
    tickers_after = sp500_tickers_as_of(2024, 6, 24)

    assert len(tickers_before) == num_tickers_2024
    assert len(tickers_after) == num_tickers_2024

    removed = {"CMA", "ILMN", "RHI"}
    added = {"CRWD", "GDDY", "KKR"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_sep_2024_bulk_swap() -> None:
    # On Sep 23, 3-for-3: Palantir, Dell, Erie replaced AAL, Etsy, Bio-Rad
    tickers_before = sp500_tickers_as_of(2024, 9, 22)
    tickers_after = sp500_tickers_as_of(2024, 9, 23)

    assert len(tickers_before) == num_tickers_2024
    assert len(tickers_after) == num_tickers_2024

    removed = {"AAL", "BIO", "ETSY"}
    added = {"DELL", "ERIE", "PLTR"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_sep_oct_2024_amtm_spinoff_and_bbwi_removal() -> None:
    # Sep 30: Amentum (AMTM) spun off from Jacobs Solutions
    tickers_sep29 = sp500_tickers_as_of(2024, 9, 29)
    tickers_sep30 = sp500_tickers_as_of(2024, 9, 30)
    assert len(tickers_sep30) == num_tickers_2024 + 1
    assert "AMTM" not in tickers_sep29
    assert "AMTM" in tickers_sep30

    # Oct 1: Bath & Body Works (BBWI) removed for market cap
    tickers_oct1 = sp500_tickers_as_of(2024, 10, 1)
    assert len(tickers_oct1) == num_tickers_2024
    assert "BBWI" in tickers_sep30
    assert "BBWI" not in tickers_oct1


def test_nov_2024_tpl_mro_swap() -> None:
    # On Nov 26, Texas Pacific Land (TPL) replaced Marathon Oil (MRO)
    _test_one_swap(datetime.date.fromisoformat("2024-11-26"), "MRO", "TPL", num_tickers_2024)


def test_dec_2024_rebalance() -> None:
    # On Dec 23, 3-for-3: APO, WDAY, LII replaced QRVO, AMTM, CTLT
    tickers_before = sp500_tickers_as_of(2024, 12, 22)
    tickers_after = sp500_tickers_as_of(2024, 12, 23)

    assert len(tickers_before) == num_tickers_2024
    assert len(tickers_after) == num_tickers_2024

    removed = {"AMTM", "CTLT", "QRVO"}
    added = {"APO", "LII", "WDAY"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
