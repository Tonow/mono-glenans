import unittest
import pandas as pd
from stage.view import filter_df


class TestFilterDF(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        data = {
            "Name": ["Alice", "Bob", "Charlie", "David", "Emily"],
            "Age": [25, 30, 22, 35, 28],
            "City": ["New York", "Los Angeles", "Chicago", "Houston", "Boston"],
            "Gender": ["Female", "Male", "Male", "Male", "Female"],
        }
        self.df = pd.DataFrame(data)

    def test_filter_single_column(self):
        columns_options = {"Name": ["Bob", "David"]}
        result = filter_df(self.df, columns_options)
        expected = self.df[self.df["Name"].isin(["Bob", "David"])]
        pd.testing.assert_frame_equal(result, expected)

    def test_filter_multiple_columns(self):
        columns_options = {"Name": ["Bob", "David"], "Age": [30, 35]}
        result = filter_df(self.df, columns_options)
        expected = self.df[
            (self.df["Name"].isin(["Bob", "David"])) & (self.df["Age"].isin([30, 35]))
        ]
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_filter_options(self):
        columns_options = {"Name": [], "Age": []}
        result = filter_df(self.df, columns_options)
        expected = (
            self.df
        )  # No filtering, so the result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(result, expected)
