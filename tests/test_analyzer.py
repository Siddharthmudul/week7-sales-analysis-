import unittest
import pandas as pd

from sales_analyzer.data_cleaner import clean_sales_data
from sales_analyzer.analyzer import basic_statistics


class TestAnalyzer(unittest.TestCase):

    def setUp(self):

        df = pd.DataFrame({
            "order_id": ["1", "2"],
            "order_date": [
                "2024-01-01",
                "2024-02-01"
            ],
            "customer_id": [
                "C001",
                "C002"
            ],
            "product_id": [
                "P001",
                "P002"
            ],
            "product_name": [
                "Laptop",
                "Phone"
            ],
            "category": [
                "Electronics",
                "Electronics"
            ],
            "quantity": [
                2,
                1
            ],
            "unit_price": [
                500,
                300
            ],
            "region": [
                "North",
                "South"
            ]
        })

        self.df = clean_sales_data(df)

    def test_total_sales(self):

        stats = basic_statistics(
            self.df
        )

        self.assertEqual(
            stats["total_sales"],
            1300
        )

    def test_total_orders(self):

        stats = basic_statistics(
            self.df
        )

        self.assertEqual(
            stats["total_orders"],
            2
        )


if __name__ == "__main__":
    unittest.main()