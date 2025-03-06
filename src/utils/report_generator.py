def generate_report(ticker, raw_metrics, formatted_metrics, esg_score, benchmark_esg):
    """
    Generate a text report summarizing the ESG analysis.
    
    Parameters:
        ticker (str): Stock ticker.
        raw_metrics (dict): Raw financial metrics.
        formatted_metrics (dict): Formatted financial metrics for display.
        esg_score (float): Calculated ESG score.
        benchmark_esg (float): ESG benchmark score for comparison.
    
    Returns:
        str: A formatted analysis report.
    """
    report = f"ESG Investment Analysis Report for {ticker}\n\n"
    
    # Financial Overview Section
    report += "Financial Overview:\n"
    report += "-" * 40 + "\n"
    for key, value in formatted_metrics.items():
        report += f"{key}: {value}\n"
    
    # ESG Analysis Section
    report += "\nESG Analysis:\n"
    report += "-" * 40 + "\n"
    report += f"Calculated ESG Score: {esg_score:.2f}\n"
    report += f"Benchmark ESG Score: {benchmark_esg}\n"
    
    # Analysis Summary
    report += "\nAnalysis Summary:\n"
    report += "-" * 40 + "\n"
    if esg_score >= benchmark_esg:
        report += "The company's ESG performance meets or exceeds the benchmark.\n"
    else:
        report += "The company's ESG performance is below the benchmark.\n"
    
    # Methodology Section
    report += "\nMethodology:\n"
    report += "-" * 40 + "\n"
    report += (
        "The ESG score was derived using sentiment analysis on the corporate report text "
        "via a pre-trained sentiment model. Financial data was sourced from Yahoo Finance.\n"
    )
    
    # Limitations Section
    report += "\nLimitations:\n"
    report += "-" * 40 + "\n"
    report += (
        "This MVP uses a simplified scoring approach. In a production system, "
        "more advanced NLP models and additional ESG factors should be incorporated."
    )
    
    return report
