import unittest
import pandas as pd

from sales_analyzer.data_cleaner import clean_sales_data


class TestDataCleaner(unittest.TestCase):

    def test_total_sales_calculation(self):

        df = pd.DataFrame({
            "order_id": ["1"],
            "order_date": ["2024-01-01"],
            "customer_id": ["C001"],
            "product_id": ["P001"],
            "product_name": ["Laptop"],
            "category": ["Electronics"],
            "quantity": [2],
            "unit_price": [500],
            "region": ["North"]
        })

        cleaned = clean_sales_data(df)

        self.assertEqual(
            cleaned.iloc[0]["total_sales"],
            1000
        )


if __name__ == "__main__":
    unittest.main()