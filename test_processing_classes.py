# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Test Processing Classes
# Desc: Unit tests for FileProcessor class in processing_classes.py
# Change Log: (Who, When, What)
# Alex Munoz, 2026-06-12, Created Script
# ------------------------------------------------------------------------------------------ #
import unittest
import json
import os
from processing_classes import FileProcessor
from data_classes import Employee


class TestFileProcessor(unittest.TestCase):
    """Tests for the FileProcessor class."""

    TEST_FILE = "test_temp_employees.json"

    def setUp(self):
        test_data = [
            {"FirstName": "Alice", "LastName": "Johnson", "ReviewDate": "2024-01-10", "ReviewRating": 4},
            {"FirstName": "Bob", "LastName": "Smith", "ReviewDate": "2024-02-20", "ReviewRating": 3}
        ]
        with open(self.TEST_FILE, "w") as f:
            json.dump(test_data, f)

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_read_loads_correct_number_of_employees(self):
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(len(result), 2)

    def test_read_loads_correct_first_name(self):
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(result[0].first_name, "Alice")

    def test_read_loads_correct_last_name(self):
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(result[0].last_name, "Johnson")

    def test_read_loads_correct_review_date(self):
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(result[0].review_date, "2024-01-10")

    def test_read_loads_correct_review_rating(self):
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(result[0].review_rating, 4)

    def test_read_file_not_found_raises_exception(self):
        with self.assertRaises(FileNotFoundError):
            FileProcessor.read_employee_data_from_file("nonexistent_file.json", [], Employee)

    def test_write_creates_valid_json(self):
        employees = [
            Employee(first_name="Carol", last_name="White", review_date="2024-03-15", review_rating=5)
        ]
        FileProcessor.write_employee_data_to_file(self.TEST_FILE, employees)
        with open(self.TEST_FILE, "r") as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["FirstName"], "Carol")
        self.assertEqual(data[0]["LastName"], "White")
        self.assertEqual(data[0]["ReviewRating"], 5)

    def test_write_and_read_roundtrip(self):
        employees = [
            Employee(first_name="Dave", last_name="Brown", review_date="2024-04-20", review_rating=2)
        ]
        FileProcessor.write_employee_data_to_file(self.TEST_FILE, employees)
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(result[0].first_name, "Dave")
        self.assertEqual(result[0].last_name, "Brown")
        self.assertEqual(result[0].review_date, "2024-04-20")
        self.assertEqual(result[0].review_rating, 2)

    def test_write_multiple_employees(self):
        employees = [
            Employee(first_name="Eve", last_name="Davis", review_date="2024-05-01", review_rating=1),
            Employee(first_name="Frank", last_name="Garcia", review_date="2024-06-15", review_rating=5)
        ]
        FileProcessor.write_employee_data_to_file(self.TEST_FILE, employees)
        result = FileProcessor.read_employee_data_from_file(self.TEST_FILE, [], Employee)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
