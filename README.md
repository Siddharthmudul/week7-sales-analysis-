Sales Data Analysis Dashboard
Project Description
A comprehensive sales data analysis system built with pandas that processes sales data, generates business insights, and creates visual reports. This project demonstrates data analysis skills for real-world business scenarios.

What I Learned
1. Pandas Fundamentals: Working with DataFrames and Series
2. Data Cleaning: Handling missing values, duplicates, and data type issues
3. Data Analysis: Calculating statistics, trends, and business metrics
4. Data Visualization: Creating informative charts and graphs
5. Report Generation: Exporting analysis results in multiple formats

Features

•	Load sales data from CSV/Excel files
•	Clean and preprocess data automatically
•	Calculate key business metrics (total sales, average, growth rates)
•	Generate monthly sales trends and reports
•	Create multiple visualization types
•	Export analysis results to Excel/CSV/Images
•	Interactive analysis through Jupyter notebooks
•	Comprehensive error handling



How to Run
bash
Copy
# Install dependencies
pip install -r requirements.txt
# Run the analyzer
python main.py
# Or use Jupyter notebooks
jupyter notebook notebooks/exploration.ipynb

Required Libraries
pandas: Data manipulation and analysis
matplotlib: Data visualization
numpy: Numerical computations
openpyxl: Excel file support
jupyter: Interactive notebooks









Sample output:
📊 SALES DATA ANALYSIS REPORT
===============================

📅 Analysis Period: Jan 2024 - Dec 2024
💰 Total Sales: $1,245,678
📈 Average Monthly Sales: $103,806
🏆 Top Product Category: Electronics ($456,789)

📈 Monthly Sales Trend:
- Jan: $98,765
- Feb: $102,345
- Mar: $115,678
- ...

📦 Top 5 Products:
1. Laptop Pro: $123,456
2. Smartphone X: $98,765
3. Wireless Headphones: $67,890
4. Tablet Air: $56,789
5. Smart Watch: $45,678

📊 Customer Insights:
- Total Customers: 1,234
- Average Order Value: $256.78
- Repeat Customers: 345 (27.9%)







Code:

import os

from sales_analyzer.data_loader import (
    load_sales_data,
    get_basic_info,
    validate_columns
)

from sales_analyzer.data_cleaner import (
    clean_sales_data,
    save_cleaned_data
)

from sales_analyzer.visualizer import (
    generate_all_visualizations
)

from sales_analyzer.reporter import (
    generate_text_report,
    save_text_report,
    export_analysis_results,
    export_excel_report
)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

RAW_DATA = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "sales_data.csv"
)

PROCESSED_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

REPORT_DIR = os.path.join(
    BASE_DIR,
    "data",
    "reports"
)

VISUALIZATION_DIR = os.path.join(
    REPORT_DIR,
    "visualizations"
)

def create_directories():
    """
    Create required project directories.
    """

    os.makedirs(
        PROCESSED_DIR,
        exist_ok=True
    )

    os.makedirs(
        REPORT_DIR,
        exist_ok=True
    )

    os.makedirs(
        VISUALIZATION_DIR,
        exist_ok=True
    )

def main():

    print("\n" + "=" * 60)
    print("        SALES DATA ANALYSIS SYSTEM")
    print("=" * 60)

    create_directories()

    try:

        # Step 1: Load data
        print("\n[1/6] Loading sales data...")

        df = load_sales_data(
            RAW_DATA
        )

        print(
            f"Loaded {len(df):,} records."
        )

        # Step 2: Explore data
        print("\n[2/6] Exploring dataset...")

        validate_columns(df)

        get_basic_info(df)

        # Step 3: Clean data
        print("\n[3/6] Cleaning data...")

        cleaned_df = clean_sales_data(
            df
        )

        cleaned_path = os.path.join(
            PROCESSED_DIR,
            "cleaned_sales_data.csv"
        )

        save_cleaned_data(
            cleaned_df,
            cleaned_path
        )

        # Step 4: Analysis
        print("\n[4/6] Performing analysis...")

        report = generate_text_report(
            cleaned_df
        )

        # Step 5: Visualizations
        print("\n[5/6] Creating visualizations...")

        paths = generate_all_visualizations(
            cleaned_df,
            VISUALIZATION_DIR
        )

        for name, path in paths.items():

            print(
                f"Created {name}: {path}"
            )

        # Step 6: Reports
        print("\n[6/6] Generating reports...")

        report_path = os.path.join(
            REPORT_DIR,
            "sales_analysis_report.txt"
        )

        save_text_report(
            report,
            report_path
        )

        export_analysis_results(
            cleaned_df,
            REPORT_DIR
        )

        excel_path = os.path.join(
            REPORT_DIR,
            "sales_analysis.xlsx"
        )

        export_excel_report(
            cleaned_df,
            excel_path
        )

        # Display final report
        print("\n")
        print(report)

        print("=" * 60)
        print("ANALYSIS COMPLETED SUCCESSFULLY")
        print("=" * 60)

        print(
            f"\nReport saved to:"
            f"\n{report_path}"
        )

        print(
            f"\nExcel report saved to:"
            f"\n{excel_path}"
        )

        print(
            f"\nCharts saved to:"
            f"\n{VISUALIZATION_DIR}"
        )

    except FileNotFoundError as error:

        print(f"\n❌ File Error: {error}")

    except ValueError as error:

        print(f"\n❌ Data Error: {error}")

    except Exception as error:

        print(
            f"\n❌ Unexpected Error: {error}"
        )

if __name__ == "__main__":
    main()

















Output:





















































































































































































































