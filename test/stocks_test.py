from pandas import DataFrame

from app.stocks import fetch_stocks_data


def test_fetch_data():
    df = fetch_stocks_data("NFLX")
    assert isinstance(df, DataFrame)
    assert "adjusted_close" in df.columns
    assert "timestamp" in df.columns
