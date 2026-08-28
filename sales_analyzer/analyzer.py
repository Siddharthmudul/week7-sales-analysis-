import pandas as pd
import numpy as np


def basic_statistics(df):
    """
    Calculate basic sales statistics.
    """

    total_sales = df["total_sales"].sum()

    total_orders = df["order_id"].nunique()

    average_order_value = (
        total_sales / total_orders
        if total_orders > 0
        else 0
    )

    unique_customers = df["customer_id"].nunique()

    unique_products = df["product_id"].nunique()

    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "unique_customers": unique_customers,
        "unique_products": unique_products
    }


def category_analysis(df):
    """
    Calculate sales by product category.
    """

    category_sales = (
        df.groupby("category")["total_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    total_sales = category_sales.sum()

    result = pd.DataFrame({
        "sales": category_sales,
        "percentage": (
            category_sales / total_sales * 100
        )
    })

    return result


def top_products(df, n=10):
    """
    Find top selling products.
    """

    result = (
        df.groupby("product_name")["total_sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

    return result


def monthly_sales(df):
    """
    Calculate monthly sales.
    """

    result = (
        df.groupby("month_period")["total_sales"]
        .sum()
        .sort_index()
    )

    return result


def monthly_growth(df):
    """
    Calculate monthly sales growth rate.
    """

    sales = monthly_sales(df)

    growth = sales.pct_change() * 100

    return growth


def customer_analysis(df):
    """
    Calculate customer purchase metrics.
    """

    customer_sales = (
        df.groupby("customer_id")["total_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    customer_orders = (
        df.groupby("customer_id")["order_id"]
        .nunique()
    )

    repeat_customers = (
        customer_orders[customer_orders > 1]
    )

    total_customers = len(customer_orders)

    repeat_customer_count = len(repeat_customers)

    repeat_percentage = (
        repeat_customer_count / total_customers * 100
        if total_customers > 0
        else 0
    )

    average_customer_value = customer_sales.mean()

    top_10_percent_count = max(
        1,
        int(np.ceil(total_customers * 0.10))
    )

    top_10_revenue = (
        customer_sales.head(top_10_percent_count).sum()
    )

    total_revenue = customer_sales.sum()

    top_10_percentage = (
        top_10_revenue / total_revenue * 100
        if total_revenue > 0
        else 0
    )

    return {
        "customer_sales": customer_sales,
        "customer_orders": customer_orders,
        "repeat_customers": repeat_customer_count,
        "repeat_percentage": repeat_percentage,
        "average_customer_value": average_customer_value,
        "top_10_percentage": top_10_percentage
    }


def peak_sales_period(df):
    """
    Find highest and lowest sales months.
    """

    sales = monthly_sales(df)

    highest_month = sales.idxmax()
    lowest_month = sales.idxmin()

    return {
        "highest_month": highest_month,
        "highest_sales": sales.max(),
        "lowest_month": lowest_month,
        "lowest_sales": sales.min(),
        "average_monthly_sales": sales.mean()
    }


def best_growth_month(df):
    """
    Find month with highest sales growth.
    """

    growth = monthly_growth(df)

    growth = growth.dropna()

    if growth.empty:
        return None, 0

    month = growth.idxmax()
    value = growth.max()

    return month, value


def sales_forecast(df, window=3):
    """
    Generate simple moving average forecast.
    """

    sales = monthly_sales(df)

    forecast = sales.rolling(
        window=window
    ).mean()

    return forecast


def geographical_analysis(df):
    """
    Calculate sales by region.
    """

    return (
        df.groupby("region")["total_sales"]
        .sum()
        .sort_values(ascending=False)
    )


def get_recommendations(df):
    """
    Generate basic business recommendations.
    """

    recommendations = []

    categories = category_analysis(df)

    if not categories.empty:

        top_category = categories.index[0]

        recommendations.append(
            f"Focus marketing on {top_category} category"
        )

    customer_info = customer_analysis(df)

    if customer_info["repeat_percentage"] < 40:
        recommendations.append(
            "Improve customer retention programs"
        )
    else:
        recommendations.append(
            "Continue strengthening customer loyalty programs"
        )

    monthly = monthly_sales(df)

    if len(monthly) >= 3:

        q4_sales = monthly[
            monthly.index.month.isin([10, 11, 12])
        ].sum()

        other_sales = monthly[
            ~monthly.index.month.isin([10, 11, 12])
        ].sum()

        if q4_sales > other_sales:
            recommendations.append(
                "Consider seasonal promotions in Q4"
            )
        else:
            recommendations.append(
                "Identify seasonal opportunities to increase Q4 sales"
            )

    if len(categories) >= 2:
        recommendations.append(
            "Expand product range in high-performing categories"
        )

    return recommendations