import unittest
import pandas as pd

from sales_analyzer.data_loader import validate_columns


class TestDataLoader(unittest.TestCase):

    def test_validate_columns(self):

        df = pd.DataFrame({
            "order_id": [],
            "order_date": [],
            "customer_id": [],
            "product_id": [],
            "product_name": [],
            "category": [],
            "quantity": [],
            "unit_price": [],
            "region": []
        })

        self.assertTrue(
            validate_columns(df)
        )


if __name__ == "__main__":
    unittest.main()