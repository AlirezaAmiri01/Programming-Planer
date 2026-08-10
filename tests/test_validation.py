import unittest
from datetime import date, timedelta
from validation import (
    validate_title,
    validate_description,
    validate_priority,
    validate_deadline
)


class TestValidation(unittest.TestCase):

    def test_valid_title_returns_title(self):
        result = validate_title("Buy groceries")
        self.assertEqual(result, "Buy groceries")

    def test_empty_title_returns_false(self):
        result = validate_title("   ")
        self.assertFalse(result)

    def test_numeric_title_returns_false(self):
        result = validate_title("12345")
        self.assertFalse(result)

    def test_valid_description_returns_description(self):
        result = validate_description("Some description")
        self.assertEqual(result, "Some description")

    def test_empty_description_returns_false(self):
        result = validate_description("")
        self.assertFalse(result)

    def test_valid_priority_returns_int(self):
        result = validate_priority("3")
        self.assertEqual(result, 3)

    def test_negative_priority_returns_false(self):
        result = validate_priority("-1")
        self.assertFalse(result)

    def test_non_numeric_priority_returns_false(self):
        result = validate_priority("abc")
        self.assertFalse(result)

    def test_empty_deadline_returns_none(self):
        result = validate_deadline("")
        self.assertIsNone(result)

    def test_valid_future_deadline_returns_date(self):
        future = date.today() + timedelta(days=5)
        future_str = future.strftime("%Y-%m-%d")
        result = validate_deadline(future_str)
        self.assertEqual(result, future)

    def test_past_deadline_raises_error(self):
        past = date.today() - timedelta(days=5)
        past_str = past.strftime("%Y-%m-%d")
        with self.assertRaises(ValueError):
            validate_deadline(past_str)

    def test_invalid_deadline_format_raises_error(self):
        with self.assertRaises(ValueError):
            validate_deadline("not-a-date")


if __name__ == "__main__":
    unittest.main()
