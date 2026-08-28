import pandas as pd
import os


def load_sales_data(file_path):
    """
    Load sales data from a CSV file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Sales data file not found: {file_path}"
        )

    try:
        df = pd.read_csv(file_path)
        return df

    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")


def get_basic_info(df):
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)

    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")

    print("\nColumns:")
    for column in df.columns:
        print(f"- {column}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Records:")
    print(df.head())


def validate_columns(df):
    """
    Check whether required columns exist.
    """

    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "region"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return True