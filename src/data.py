import pandas as pd
import yfinance as yf


def get_closing_prices(tickers: str, period: str) -> pd.Series:
    """Obtain the close price of a company in the market share.

    Parameters
    ----------
    tickers : str
        unique indentify of public traded companies (E.g: "MSFT" (Microsoft Corporation))
    period : str
        number of period to be downloaded

    Returns
    -------
    pd.Series
        A serie with the date (index) and close prices (column)
    """
    stock_data = yf.download(tickers=tickers, period=period)
    stock_data = stock_data.rename(columns={"Close": "close"})
    return stock_data["close"]
