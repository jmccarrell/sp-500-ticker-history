import datetime

from sp_500_ticker_history import sp500_tickers_as_of

from .helpers import _test_at_year_boundary, _test_one_swap

num_tickers_2023 = 503


def test_jan1_2023_count() -> None:
    assert len(sp500_tickers_as_of(2023, 1, 1)) == num_tickers_2023


def test_year_boundary_2023_2024() -> None:
    _test_at_year_boundary(2024)


def test_jan_2023_gehc_spinoff_and_vno_removal() -> None:
    # Jan 4: GE HealthCare (GEHC) spun off from GE
    tickers_jan3 = sp500_tickers_as_of(2023, 1, 3)
    tickers_jan4 = sp500_tickers_as_of(2023, 1, 4)
    assert len(tickers_jan3) == num_tickers_2023
    assert len(tickers_jan4) == num_tickers_2023 + 1
    assert "GEHC" not in tickers_jan3
    assert "GEHC" in tickers_jan4

    # Jan 5: Vornado Realty (VNO) removed for market cap
    tickers_jan5 = sp500_tickers_as_of(2023, 1, 5)
    assert len(tickers_jan5) == num_tickers_2023
    assert "VNO" in tickers_jan4
    assert "VNO" not in tickers_jan5


def test_mar_2023_bank_failures() -> None:
    # Mar 15: SVB and Signature Bank placed into FDIC receivership
    # Replaced by Bunge (BG) and Insulet (PODD)
    tickers_before = sp500_tickers_as_of(2023, 3, 14)
    tickers_after = sp500_tickers_as_of(2023, 3, 15)

    assert len(tickers_before) == num_tickers_2023
    assert len(tickers_after) == num_tickers_2023

    removed = {"SBNY", "SIVB"}
    added = {"BG", "PODD"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_mar_2023_fico_lumn_swap() -> None:
    # Mar 20: Fair Isaac (FICO) replaced Lumen Technologies (LUMN)
    _test_one_swap(datetime.date.fromisoformat("2023-03-20"), "LUMN", "FICO", num_tickers_2023)


def test_may_2023_axon_frc_swap() -> None:
    # May 4: Axon (AXON) replaced First Republic Bank (FRC) after FDIC receivership
    _test_one_swap(datetime.date.fromisoformat("2023-05-04"), "FRC", "AXON", num_tickers_2023)


def test_jun_2023_panw_dish_swap() -> None:
    # Jun 20: Palo Alto Networks (PANW) replaced Dish Network (DISH)
    _test_one_swap(datetime.date.fromisoformat("2023-06-20"), "DISH", "PANW", num_tickers_2023)


def test_aug_2023_kvue_aap_swap() -> None:
    # Aug 25: Kenvue (KVUE) replaced Advance Auto Parts (AAP)
    _test_one_swap(datetime.date.fromisoformat("2023-08-25"), "AAP", "KVUE", num_tickers_2023)


def test_sep_2023_bulk_swap() -> None:
    # Sep 18: Blackstone (BX) and Airbnb (ABNB) replaced Lincoln National (LNC) and Newell (NWL)
    tickers_before = sp500_tickers_as_of(2023, 9, 17)
    tickers_after = sp500_tickers_as_of(2023, 9, 18)

    assert len(tickers_before) == num_tickers_2023
    assert len(tickers_after) == num_tickers_2023

    removed = {"LNC", "NWL"}
    added = {"ABNB", "BX"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_oct_2023_vlto_spinoff_and_dxc_removal() -> None:
    # Oct 2: Veralto (VLTO) spun off from Danaher
    tickers_oct1 = sp500_tickers_as_of(2023, 10, 1)
    tickers_oct2 = sp500_tickers_as_of(2023, 10, 2)
    assert len(tickers_oct2) == num_tickers_2023 + 1
    assert "VLTO" not in tickers_oct1
    assert "VLTO" in tickers_oct2

    # Oct 3: DXC Technology removed for market cap
    tickers_oct3 = sp500_tickers_as_of(2023, 10, 3)
    assert len(tickers_oct3) == num_tickers_2023
    assert "DXC" in tickers_oct2
    assert "DXC" not in tickers_oct3


def test_oct_2023_hubb_lulu_swap() -> None:
    # Oct 18: Hubbell (HUBB) and Lululemon (LULU) replaced Organon (OGN) and Activision (ATVI)
    tickers_before = sp500_tickers_as_of(2023, 10, 17)
    tickers_after = sp500_tickers_as_of(2023, 10, 18)

    assert len(tickers_before) == num_tickers_2023
    assert len(tickers_after) == num_tickers_2023

    removed = {"ATVI", "OGN"}
    added = {"HUBB", "LULU"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after


def test_dec_2023_rebalance() -> None:
    # Dec 18: Uber, Jabil, Builders FirstSource replaced Sealed Air, Alaska Air, SolarEdge
    tickers_before = sp500_tickers_as_of(2023, 12, 17)
    tickers_after = sp500_tickers_as_of(2023, 12, 18)

    assert len(tickers_before) == num_tickers_2023
    assert len(tickers_after) == num_tickers_2023

    removed = {"ALK", "SEDG", "SEE"}
    added = {"BLDR", "JBL", "UBER"}

    for ticker in removed:
        assert ticker in tickers_before
        assert ticker not in tickers_after
    for ticker in added:
        assert ticker not in tickers_before
        assert ticker in tickers_after
