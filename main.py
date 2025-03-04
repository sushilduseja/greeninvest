import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

from data_collection import get_company_data
from esg_analysis import analyze_esg
from report_generator import generate_report

# Set page configuration
st.set_page_config(page_title="GreenInvest ESG Analyzer", layout="wide")

st.title("GreenInvest: AI-Powered ESG Portfolio Analysis Tool")

# Sidebar: Input company ticker
ticker = st.sidebar.text_input("Enter Company Ticker", "AAPL")

# Data Collection: Retrieve and display company data
company_data = get_company_data(ticker)
st.header(f"{ticker} - Company Financial Data")
st.dataframe(company_data)

# ESG Analysis Section
st.header("ESG Analysis from Corporate Report")
sample_report = st.text_area("Paste Corporate ESG Report Text", 
                              "Enter corporate report text here...")

if st.button("Run ESG Analysis"):
    esg_score, sentiment_result = analyze_esg(sample_report)
    st.subheader("ESG Analysis Result")
    st.write(f"Calculated ESG Score: **{esg_score:.2f}**")
    st.write("Sentiment Analysis Detail:", sentiment_result)
    
    # Save ESG score for report generation
    current_esg_score = esg_score
else:
    current_esg_score = None

# Portfolio Visualization Section
st.header("Stock Price Visualization")
# Retrieve historical stock data using yfinance (1-year period)
stock_data = yf.download(ticker, period="1y")
if not stock_data.empty:
    # Reset the multi-index if present and select the Close column
    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data = stock_data.loc[:, ('Close', slice(None))].droplevel(1, axis=1)
    
    fig = px.line(stock_data, 
                  x=stock_data.index, 
                  y='Close',
                  title=f"{ticker} Stock Price (Last 1 Year)")
    st.plotly_chart(fig)
else:
    st.write("Unable to retrieve stock data.")

# ESG Benchmark Comparison
st.header("ESG Benchmark Comparison")
# For MVP, we use a dummy benchmark ESG score.
benchmark_esg = 0.75
st.write(f"Benchmark ESG Score: **{benchmark_esg}**")

# Report Generation Section
st.header("Generate Analysis Report")
if st.button("Generate Report"):
    if current_esg_score is None:
        st.error("Please run the ESG analysis first.")
    else:
        report_text = generate_report(ticker, company_data, current_esg_score, benchmark_esg)
        st.download_button("Download Report", report_text, file_name="esg_report.txt")
