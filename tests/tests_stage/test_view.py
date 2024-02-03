import unittest
import pandas as pd
from stage.view import filter_df
from datetime import date


class TestFilterDF(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        data = {
            "Name": ["Alice", "Bob", "Charlie", "David", "Emily"],
            "Age": [25, 30, 22, 35, 28],
            "City": ["New York", "Los Angeles", "Chicago", "Houston", "Boston"],
            "Gender": ["Female", "Male", "Male", "Male", "Female"],
            "Début": [
                date(2025, 1, 8),
                date(2025, 1, 9),
                date(2025, 1, 10),
                date(2025, 1, 11),
                date(2025, 1, 12),
            ],
            "Fin": [
                date(2025, 1, 9),
                date(2025, 1, 10),
                date(2025, 1, 11),
                date(2025, 1, 12),
                date(2025, 1, 13),
            ],
        }
        self.df = pd.DataFrame(data)

    def test_filter_date_column(self):
        columns_options = {"Name": [], "Age": []}
        start_date = date(2025, 1, 11)
        end_date = date(2025, 1, 13)
        result = filter_df(self.df, columns_options, start_date, end_date)
        expected_start = self.df[
            self.df["Début"].isin([date(2025, 1, 11), date(2025, 1, 12)])
        ]
        expected_end = self.df[
            self.df["Fin"].isin([date(2025, 1, 12), date(2025, 1, 13)])
        ]
        pd.testing.assert_frame_equal(result, expected_start)
        pd.testing.assert_frame_equal(result, expected_end)

    def test_filter_single_column(self):
        columns_options = {"Name": ["Bob", "David"]}
        start_date = date(2025, 1, 8)
        end_date = date(2025, 1, 12)
        result = filter_df(self.df, columns_options, start_date, end_date)
        expected = self.df[self.df["Name"].isin(["Bob", "David"])]
        pd.testing.assert_frame_equal(result, expected)

    def test_filter_multiple_columns(self):
        columns_options = {"Name": ["Bob", "David"], "Age": [30, 35]}
        start_date = date(2025, 1, 8)
        end_date = date(2025, 1, 12)
        result = filter_df(self.df, columns_options, start_date, end_date)
        expected = self.df[
            (self.df["Name"].isin(["Bob", "David"])) & (self.df["Age"].isin([30, 35]))
        ]
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_filter_options(self):
        columns_options = {"Name": [], "Age": []}
        start_date = date(2022, 1, 8)
        end_date = date(2026, 1, 12)
        result = filter_df(self.df, columns_options, start_date, end_date)
        expected = (
            self.df
        )  # No filtering, so the result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(result, expected)
