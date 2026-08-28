import pandas as pd


def clean_sales_data(df):
    """
    Clean the sales dataset.
    """

    df = df.copy()

    print("\n" + "=" * 60)
    print("DATA CLEANING")
    print("=" * 60)

    # Remove duplicate records
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        print(f"Removing {duplicate_count} duplicate records...")
        df = df.drop_duplicates()
    else:
        print("No duplicate records found.")

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    # Convert numeric columns
    numeric_columns = [
        "quantity",
        "unit_price"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove records with invalid dates
    invalid_dates = df["order_date"].isnull().sum()

    if invalid_dates > 0:
        print(f"Removing {invalid_dates} records with invalid dates.")
        df = df.dropna(subset=["order_date"])

    # Handle quantity
    df["quantity"] = df["quantity"].fillna(1)

    # Handle unit price using median
    df["unit_price"] = df["unit_price"].fillna(
        df["unit_price"].median()
    )

    # Handle text columns
    text_columns = [
        "customer_id",
        "product_id",
        "product_name",
        "category",
        "region"
    ]

    for column in text_columns:
        df[column] = df[column].fillna("Unknown")
        df[column] = df[column].astype(str).str.strip()

    # Remove invalid quantities
    df = df[df["quantity"] > 0]

    # Remove invalid prices
    df = df[df["unit_price"] >= 0]

    # Create total sales column
    df["total_sales"] = (
        df["quantity"] * df["unit_price"]
    )

    # Create year/month columns
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["month_name"] = df["order_date"].dt.strftime("%B")

    # Create month period
    df["month_period"] = (
        df["order_date"].dt.to_period("M")
    )

    df = df.sort_values("order_date")

    print(f"Cleaned records: {len(df)}")

    return df


def save_cleaned_data(df, output_path):
    """
    Save cleaned data to CSV.
    """

    df.to_csv(
        output_path,
        index=False
    )

    print(f"\nCleaned data saved to: {output_path}")