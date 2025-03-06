import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

from data.data_collection import get_company_data
from analysis.esg_analysis import analyze_esg
from utils.report_generator import generate_report

# Set page configuration
st.set_page_config(page_title="GreenInvest ESG Analyzer", layout="wide")

st.title("GreenInvest: AI-Powered ESG Portfolio Analysis Tool")

# Sidebar: Input company ticker
ticker = st.sidebar.text_input("Enter Company Ticker", "AAPL")

# Initialize session state for ESG score if it doesn't exist
if 'current_esg_score' not in st.session_state:
    st.session_state.current_esg_score = None

# Data Collection: Retrieve and display company data
raw_metrics, formatted_metrics = get_company_data(ticker)
st.header(f"{ticker} - Financial Overview")

# Create three columns for key metrics
col1, col2, col3 = st.columns(3)

# Market performance metrics
with col1:
    st.subheader("Market Performance")
    st.metric(
        label="Market Cap",
        value=formatted_metrics.get('Market Cap', 'N/A'),
        delta=None
    )
    st.metric(
        label="P/E Ratio",
        value=formatted_metrics.get('P/E Ratio', 'N/A'),
        delta=None
    )
    st.metric(
        label="Revenue Growth",
        value=formatted_metrics.get('Revenue Growth', 'N/A'),
        delta=formatted_metrics.get('Revenue Growth', 'N/A'),
        delta_color="normal"
    )

# Profitability metrics
with col2:
    st.subheader("Profitability")
    st.metric(
        label="Profit Margin",
        value=formatted_metrics.get('Profit Margin', 'N/A'),
        delta=None
    )
    st.metric(
        label="Operating Margin",
        value=formatted_metrics.get('Operating Margin', 'N/A'),
        delta=None
    )
    st.metric(
        label="Return on Equity",
        value=formatted_metrics.get('Return on Equity', 'N/A'),
        delta=None
    )

# Financial health metrics
with col3:
    st.subheader("Financial Health")
    st.metric(
        label="Total Revenue",
        value=formatted_metrics.get('Total Revenue', 'N/A'),
        delta=None
    )
    st.metric(
        label="Debt to Equity",
        value=formatted_metrics.get('Debt to Equity', 'N/A'),
        delta=None
    )
    st.metric(
        label="Current Ratio",
        value=formatted_metrics.get('Current Ratio', 'N/A'),
        delta=None
    )

# Add a divider
st.markdown("---")

# ESG Analysis Section
st.header("ESG Analysis from Corporate Report")
sample_report = st.text_area("Paste Corporate ESG Report Text", 
                              "Enter corporate report text here...")

if st.button("Run ESG Analysis"):
    esg_score, sentiment_result = analyze_esg(sample_report)
    st.subheader("ESG Analysis Result")
    st.write(f"Calculated ESG Score: **{esg_score:.2f}**")
    st.write("Sentiment Analysis Detail:", sentiment_result)
    
    # Save ESG score in session state
    st.session_state.current_esg_score = esg_score

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
    if st.session_state.current_esg_score is None:
        st.error("Please run the ESG analysis first.")
    else:
        report_text = generate_report(ticker, raw_metrics, formatted_metrics,
                                    st.session_state.current_esg_score, 
                                    benchmark_esg)
        st.download_button("Download Report", report_text, 
                          file_name="esg_report.txt")
