def generate_report(ticker, company_data, esg_score, benchmark_esg):
    """
    Generate a text report summarizing the ESG analysis.
    
    Parameters:
        ticker (str): Stock ticker.
        company_data (pd.DataFrame): Company financial info.
        esg_score (float): Calculated ESG score.
        benchmark_esg (float): ESG benchmark score for comparison.
    
    Returns:
        str: A formatted analysis report.
    """
    report = f"ESG Investment Analysis Report for {ticker}\n\n"
    report += "Company Financial Data:\n"
    report += str(company_data) + "\n\n"
    report += f"Calculated ESG Score: {esg_score:.2f}\n"
    report += f"Benchmark ESG Score: {benchmark_esg}\n\n"
    report += "Analysis:\n"
    if esg_score >= benchmark_esg:
        report += "The company's ESG performance meets or exceeds the benchmark.\n"
    else:
        report += "The company's ESG performance is below the benchmark.\n"
    
    report += "\nMethodology:\n"
    report += (
        "The ESG score was derived using sentiment analysis on the corporate report text "
        "via a pre-trained sentiment model. Financial data was sourced from Yahoo Finance.\n"
    )
    report += "\nLimitations:\n"
    report += (
        "This MVP uses a simplified scoring approach. In a production system, "
        "more advanced NLP models and additional ESG factors should be incorporated."
    )
    
    return report
