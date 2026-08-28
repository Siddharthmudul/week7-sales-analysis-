import matplotlib.pyplot as plt
import os


def create_output_directory(output_dir):
    """
    Create visualization directory.
    """

    os.makedirs(output_dir, exist_ok=True)


def sales_trend_chart(df, output_dir):
    """
    Create sales trend line chart.
    """

    monthly = (
        df.groupby("month_period")["total_sales"]
        .sum()
    )

    plt.figure(figsize=(12, 6))

    plt.plot(
        monthly.index.astype(str),
        monthly.values,
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        "sales_trend.png"
    )

    plt.savefig(path, dpi=300)
    plt.close()

    return path


def category_pie_chart(df, output_dir):
    """
    Create product category pie chart.
    """

    category_sales = (
        df.groupby("category")["total_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        category_sales.values,
        labels=category_sales.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Sales by Product Category")

    path = os.path.join(
        output_dir,
        "category_sales_pie.png"
    )

    plt.savefig(path, dpi=300)
    plt.close()

    return path


def monthly_sales_bar_chart(df, output_dir):
    """
    Create monthly sales bar chart.
    """

    monthly = (
        df.groupby("month_period")["total_sales"]
        .sum()
    )

    plt.figure(figsize=(12, 6))

    plt.bar(
        monthly.index.astype(str),
        monthly.values
    )

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        "monthly_sales_bar.png"
    )

    plt.savefig(path, dpi=300)
    plt.close()

    return path


def geographical_sales_chart(df, output_dir):
    """
    Create geographical sales distribution chart.
    """

    region_sales = (
        df.groupby("region")["total_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    plt.bar(
        region_sales.index,
        region_sales.values
    )

    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    path = os.path.join(
        output_dir,
        "geographical_sales.png"
    )

    plt.savefig(path, dpi=300)
    plt.close()

    return path


def create_dashboard(df, output_dir):
    """
    Create a dashboard containing multiple charts.
    """

    monthly = (
        df.groupby("month_period")["total_sales"]
        .sum()
    )

    categories = (
        df.groupby("category")["total_sales"]
        .sum()
    )

    regions = (
        df.groupby("region")["total_sales"]
        .sum()
    )

    plt.figure(figsize=(14, 10))

    # Chart 1 - Monthly trend
    plt.subplot(2, 2, 1)

    plt.plot(
        monthly.index.astype(str),
        monthly.values,
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xticks(rotation=45)

    # Chart 2 - Categories
    plt.subplot(2, 2, 2)

    plt.pie(
        categories.values,
        labels=categories.index,
        autopct="%1.1f%%"
    )

    plt.title("Category Distribution")

    # Chart 3 - Regions
    plt.subplot(2, 2, 3)

    plt.bar(
        regions.index,
        regions.values
    )

    plt.title("Regional Sales")
    plt.xticks(rotation=45)

    # Chart 4 - Monthly bars
    plt.subplot(2, 2, 4)

    plt.bar(
        monthly.index.astype(str),
        monthly.values
    )

    plt.title("Monthly Sales")
    plt.xticks(rotation=45)

    plt.suptitle(
        "SALES ANALYSIS DASHBOARD",
        fontsize=18
    )

    plt.tight_layout()

    path = os.path.join(
        output_dir,
        "sales_dashboard.png"
    )

    plt.savefig(path, dpi=300)
    plt.close()

    return path


def generate_all_visualizations(df, output_dir):
    """
    Generate all required visualizations.
    """

    create_output_directory(output_dir)

    paths = {}

    paths["trend"] = sales_trend_chart(
        df,
        output_dir
    )

    paths["category"] = category_pie_chart(
        df,
        output_dir
    )

    paths["monthly"] = monthly_sales_bar_chart(
        df,
        output_dir
    )

    paths["geographical"] = geographical_sales_chart(
        df,
        output_dir
    )

    paths["dashboard"] = create_dashboard(
        df,
        output_dir
    )

    return paths