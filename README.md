# GreenInvest: ESG Investment Analysis Tool

An AI-powered dashboard for analyzing Environmental, Social, and Governance (ESG) factors in investment portfolios using sentiment analysis and public financial data.

## Features

- Real-time financial data analysis via Yahoo Finance API
- ESG scoring using sentiment analysis of corporate reports
- Interactive stock price visualization
- Automated ESG report generation
- Industry benchmark comparisons
- Fallback sentiment analysis when NLTK is unavailable

## Quick Start

1. Setup environment:
```bash
# Create and activate virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run main.py
```

3. Access the dashboard at http://localhost:8501

## Usage Guide

1. Enter a company ticker symbol (e.g., "AAPL" for Apple Inc.)
2. Paste the company's ESG report text into the analysis section
3. Click "Run ESG Analysis" to get the ESG score
4. View the interactive stock price chart
5. Generate and download a detailed ESG analysis report

## Technical Details

- **Data Sources**: Yahoo Finance API
- **Analysis**: NLTK VADER sentiment analysis with keyword-based fallback
- **Frontend**: Streamlit dashboard
- **Visualization**: Plotly Express charts

## Limitations

- Analysis based on publicly available data
- Simplified scoring methodology
- Basic sentiment analysis approach
- Limited to companies with public ESG reports

## Future Enhancements

- [ ] Additional data sources integration
- [ ] Advanced NLP models for text analysis
- [ ] Custom industry benchmarks
- [ ] Historical ESG trend analysis
- [ ] Portfolio-level aggregation

## Contributing

Contributions welcome! Please create an issue or submit a pull request.

## License

MIT License