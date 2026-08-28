import os

from sales_analyzer.data_loader import load_sales_data, get_basic_info, validate_columns
from sales_analyzer.data_cleaner import clean_sales_data, save_cleaned_data
from sales_analyzer.visualizer import generate_all_visualizations
from sales_analyzer.reporter import (
    generate_text_report,
    save_text_report,
    export_analysis_results,
    export_excel_report,
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA = os.path.join(BASE_DIR, "data", "raw", "sales_data.csv.txt")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
REPORT_DIR = os.path.join(BASE_DIR, "data", "reports")
VISUALIZATION_DIR = os.path.join(REPORT_DIR, "visualizations")


def create_directories():
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(VISUALIZATION_DIR, exist_ok=True)


def main():
    print("\n" + "=" * 60)
    print("        SALES DATA ANALYSIS SYSTEM")
    print("=" * 60)

    create_directories()

    try:
        print("\n[1/6] Loading sales data...")
        data = load_sales_data(RAW_DATA)
        print(f"Loaded {len(data):,} records.")

        print("\n[2/6] Exploring dataset...")
        validate_columns(data)
        get_basic_info(data)

        print("\n[3/6] Cleaning data...")
        cleaned_data = clean_sales_data(data)
        save_cleaned_data(
            cleaned_data,
            os.path.join(PROCESSED_DIR, "cleaned_sales_data.csv"),
        )

        print("\n[4/6] Performing analysis...")
        report = generate_text_report(cleaned_data)

        print("\n[5/6] Creating visualizations...")
        paths = generate_all_visualizations(cleaned_data, VISUALIZATION_DIR)
        for name, path in paths.items():
            print(f"Created {name}: {path}")

        print("\n[6/6] Generating reports...")
        report_path = os.path.join(REPORT_DIR, "sales_analysis_report.txt")
        save_text_report(report, report_path)
        export_analysis_results(cleaned_data, REPORT_DIR)

        excel_path = os.path.join(REPORT_DIR, "sales_analysis.xlsx")
        export_excel_report(cleaned_data, excel_path)

        print("\n" + report)
        print("=" * 60)
        print("ANALYSIS COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print(f"\nReport saved to:\n{report_path}")
        print(f"\nExcel report saved to:\n{excel_path}")
        print(f"\nCharts saved to:\n{VISUALIZATION_DIR}")

    except FileNotFoundError as error:
        print(f"\nFile Error: {error}")
    except ValueError as error:
        print(f"\nData Error: {error}")
    except Exception as error:
        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()
