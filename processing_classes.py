# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Processing Classes
# Desc: This module contains the FileProcessor class for reading and writing employee data
# Change Log: (Who, When, What)
# Alex Munoz, 2026-06-12, Created Script
# ------------------------------------------------------------------------------------------ #
import json
from data_classes import Employee


class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    ChangeLog: (Who, When, What)
    Alex Munoz, 2026-06-12, Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """
        Reads data from a JSON file and loads it into a list of Employee objects.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :param file_name: string with the name of the file to read from
        :param employee_data: list to be filled with Employee objects
        :param employee_type: a reference to the Employee class
        :return: list of Employee objects
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Converts a list of Employee objects to dictionaries and writes them to a JSON file.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :param file_name: string with the name of the file to write to
        :param employee_data: list of Employee objects to be written to the file
        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:
                employee_json: dict = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }
                list_of_dictionary_data.append(employee_json)
            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=2)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception:
            raise Exception("There was a non-specific error!")
