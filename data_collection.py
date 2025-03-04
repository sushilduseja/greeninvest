import yfinance as yf
import pandas as pd

def get_company_data(ticker):
    """
    Fetch company financial data using yfinance.
    
    Parameters:
        ticker (str): Stock ticker symbol.
    
    Returns:
        pd.DataFrame: A DataFrame containing a subset of company info.
    """
    ticker_data = yf.Ticker(ticker)
    info = ticker_data.info  # Get general company info
    df = pd.DataFrame.from_dict(info, orient='index', columns=['Value'])
    # Return a small sample of the info for brevity
    return df.head(10)
