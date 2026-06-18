# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Test Presentation Classes
# Desc: Unit tests for IO class in presentation_classes.py
# Change Log: (Who, When, What)
# Alex Munoz, 2026-06-12, Created Script
# ------------------------------------------------------------------------------------------ #
import unittest
from unittest.mock import patch
from io import StringIO
from presentation_classes import IO
from data_classes import Employee


class TestIO(unittest.TestCase):
    """Tests for the IO class."""

    def test_output_error_messages_prints_message(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            IO.output_error_messages("Test error message")
            output = mock_out.getvalue()
        self.assertIn("Test error message", output)

    def test_output_error_messages_prints_technical_details_when_error_provided(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            IO.output_error_messages("Test error", ValueError("bad value"))
            output = mock_out.getvalue()
        self.assertIn("Technical Error Message", output)

    def test_output_error_messages_no_technical_details_without_error(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            IO.output_error_messages("Simple message")
            output = mock_out.getvalue()
        self.assertNotIn("Technical Error Message", output)

    def test_input_menu_choice_returns_valid_choice(self):
        for choice in ("1", "2", "3", "4"):
            with patch('builtins.input', return_value=choice):
                with patch('sys.stdout', new_callable=StringIO):
                    result = IO.input_menu_choice()
            self.assertEqual(result, choice)

    def test_input_menu_choice_invalid_still_returns_input(self):
        with patch('builtins.input', return_value="9"):
            with patch('sys.stdout', new_callable=StringIO):
                result = IO.input_menu_choice()
        self.assertEqual(result, "9")

    def test_output_employee_data_displays_rating_5_label(self):
        employees = [Employee(first_name="Alice", last_name="Johnson", review_date="2024-01-10", review_rating=5)]
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            IO.output_employee_data(employees)
            output = mock_out.getvalue()
        self.assertIn("Leading", output)
        self.assertIn("Alice", output)

    def test_output_employee_data_displays_rating_1_label(self):
        employees = [Employee(first_name="Bob", last_name="Smith", review_date="2024-02-10", review_rating=1)]
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            IO.output_employee_data(employees)
            output = mock_out.getvalue()
        self.assertIn("Not Meeting Expectations", output)

    def test_output_employee_data_displays_all_ratings(self):
        labels = {1: "Not Meeting Expectations", 2: "Building", 3: "Solid", 4: "Strong", 5: "Leading"}
        for rating, label in labels.items():
            employees = [Employee(first_name="Test", last_name="User", review_date="2024-01-01", review_rating=rating)]
            with patch('sys.stdout', new_callable=StringIO) as mock_out:
                IO.output_employee_data(employees)
                output = mock_out.getvalue()
            self.assertIn(label, output)

    def test_input_employee_data_valid_input(self):
        inputs = ["Alice", "Johnson", "2024-01-10", "4"]
        with patch('builtins.input', side_effect=inputs):
            result = IO.input_employee_data([], Employee)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].first_name, "Alice")
        self.assertEqual(result[0].last_name, "Johnson")
        self.assertEqual(result[0].review_date, "2024-01-10")
        self.assertEqual(result[0].review_rating, 4)

    def test_input_employee_data_invalid_first_name_returns_empty_list(self):
        inputs = ["Alice123", "Johnson", "2024-01-10", "4"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=StringIO):
                result = IO.input_employee_data([], Employee)
        self.assertEqual(len(result), 0)

    def test_input_employee_data_invalid_rating_returns_empty_list(self):
        inputs = ["Alice", "Johnson", "2024-01-10", "9"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=StringIO):
                result = IO.input_employee_data([], Employee)
        self.assertEqual(len(result), 0)

    def test_input_employee_data_invalid_date_returns_empty_list(self):
        inputs = ["Alice", "Johnson", "bad-date", "4"]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=StringIO):
                result = IO.input_employee_data([], Employee)
        self.assertEqual(len(result), 0)

    def test_input_employee_data_appends_to_existing_list(self):
        existing = [Employee(first_name="Bob", last_name="Smith", review_date="2024-01-01", review_rating=3)]
        inputs = ["Alice", "Johnson", "2024-01-10", "4"]
        with patch('builtins.input', side_effect=inputs):
            result = IO.input_employee_data(existing, Employee)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
