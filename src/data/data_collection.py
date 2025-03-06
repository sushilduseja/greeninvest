import yfinance as yf
import pandas as pd

def get_company_data(ticker):
    """
    Fetch key financial metrics with both raw and formatted values.
    
    Parameters:
        ticker (str): Stock ticker symbol.
    
    Returns:
        tuple: (raw_metrics dict, formatted_metrics dict)
    """
    try:
        ticker_data = yf.Ticker(ticker)
        
        # Get raw values
        raw_metrics = {
            'Market Cap': ticker_data.info.get('marketCap', 0),
            'P/E Ratio': ticker_data.info.get('forwardPE', 0),
            'Revenue Growth': ticker_data.info.get('revenueGrowth', 0),
            'Profit Margin': ticker_data.info.get('profitMargins', 0),
            'Operating Margin': ticker_data.info.get('operatingMargins', 0),
            'Return on Equity': ticker_data.info.get('returnOnEquity', 0),
            'Total Revenue': ticker_data.info.get('totalRevenue', 0),
            'Gross Profits': ticker_data.info.get('grossProfits', 0),
            'Debt to Equity': ticker_data.info.get('debtToEquity', 0),
            'Current Ratio': ticker_data.info.get('currentRatio', 0)
        }
        
        # Create formatted values
        formatted_metrics = {}
        for key, value in raw_metrics.items():
            if isinstance(value, (int, float)):
                if any(metric in key for metric in ['Margin', 'Growth', 'Return']):
                    formatted_metrics[key] = f"{value:.1%}"
                elif 'Market Cap' in key or 'Revenue' in key or 'Profits' in key:
                    if value > 1_000_000_000:
                        formatted_metrics[key] = f"${value/1_000_000_000:.1f}B"
                    else:
                        formatted_metrics[key] = f"${value/1_000_000:.1f}M"
                else:
                    formatted_metrics[key] = f"{value:.2f}"
            else:
                formatted_metrics[key] = 'N/A'
                
        return raw_metrics, formatted_metrics
        
    except Exception as e:
        print(f"Error fetching financial data for {ticker}: {str(e)}")
        return {}, {}
