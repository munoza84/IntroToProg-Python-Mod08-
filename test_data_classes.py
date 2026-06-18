# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Test Data Classes
# Desc: Unit tests for Person and Employee classes in data_classes.py
# Change Log: (Who, When, What)
# Alex Munoz, 2026-06-12, Created Script
# ------------------------------------------------------------------------------------------ #
import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    """Tests for the Person class."""

    def test_first_name_stores_correctly(self):
        p = Person(first_name="John", last_name="Doe")
        self.assertEqual(p.first_name, "John")

    def test_first_name_title_case(self):
        p = Person(first_name="john", last_name="doe")
        self.assertEqual(p.first_name, "John")

    def test_first_name_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            Person(first_name="J0hn", last_name="Doe")

    def test_last_name_stores_correctly(self):
        p = Person(first_name="John", last_name="Doe")
        self.assertEqual(p.last_name, "Doe")

    def test_last_name_title_case(self):
        p = Person(first_name="john", last_name="doe")
        self.assertEqual(p.last_name, "Doe")

    def test_last_name_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            Person(first_name="John", last_name="D0e")

    def test_str_returns_comma_separated(self):
        p = Person(first_name="John", last_name="Doe")
        self.assertEqual(str(p), "John,Doe")

    def test_default_values(self):
        p = Person()
        self.assertEqual(p.first_name, "")
        self.assertEqual(p.last_name, "")


class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def test_defaults(self):
        e = Employee()
        self.assertEqual(e.first_name, "")
        self.assertEqual(e.last_name, "")
        self.assertEqual(e.review_date, "1900-01-01")
        self.assertEqual(e.review_rating, 3)

    def test_review_date_valid(self):
        e = Employee(first_name="Jane", last_name="Smith", review_date="2024-01-15", review_rating=4)
        self.assertEqual(e.review_date, "2024-01-15")

    def test_review_date_invalid_month_raises_value_error(self):
        with self.assertRaises(ValueError):
            Employee(first_name="Jane", last_name="Smith", review_date="2024-13-01", review_rating=4)

    def test_review_date_wrong_format_raises_value_error(self):
        with self.assertRaises(ValueError):
            Employee(first_name="Jane", last_name="Smith", review_date="01-15-2024", review_rating=4)

    def test_review_rating_all_valid_values(self):
        for rating in (1, 2, 3, 4, 5):
            e = Employee(first_name="Jane", last_name="Smith", review_date="2024-01-15", review_rating=rating)
            self.assertEqual(e.review_rating, rating)

    def test_review_rating_too_high_raises_value_error(self):
        with self.assertRaises(ValueError):
            Employee(first_name="Jane", last_name="Smith", review_date="2024-01-15", review_rating=6)

    def test_review_rating_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            Employee(first_name="Jane", last_name="Smith", review_date="2024-01-15", review_rating=0)

    def test_str_returns_comma_separated(self):
        e = Employee(first_name="Jane", last_name="Smith", review_date="2024-01-15", review_rating=4)
        self.assertEqual(str(e), "Jane,Smith,2024-01-15,4")

    def test_inherits_name_validation_from_person(self):
        with self.assertRaises(ValueError):
            Employee(first_name="Jane123", last_name="Smith", review_date="2024-01-15", review_rating=4)


if __name__ == "__main__":
    unittest.main()
