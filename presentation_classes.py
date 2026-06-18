# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Presentation Classes
# Desc: This module contains the IO class for managing user input and output
# Change Log: (Who, When, What)
#   Alex Munoz, 2026-06-12, Created Script
# ------------------------------------------------------------------------------------------ #
from data_classes import Employee


class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    ChangeLog: (Who, When, What)
    Alex Munoz, 2026-06-12, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message, and optionally the technical exception details.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu of choices to the user.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :param menu: string containing the menu text to display
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Gets and validates a menu choice from the user.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :return: string with the user's menu choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays the employee name and review rating for each Employee object in the list.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :param employee_data: list of Employee objects to be displayed
        :return: None
        """
        message: str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"
            print(message.format(employee.first_name, employee.last_name))
        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """
        Prompts the user for an employee's first name, last name, review date, and review rating,
        creates an Employee object, and appends it to the list.

        ChangeLog: (Who, When, What)
        Alex Munoz, 2026-06-12, Created function

        :param employee_data: list of Employee objects to be filled with input data
        :param employee_type: a reference to the Employee class
        :return: list of Employee objects
        """
        try:
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date (YYYY-MM-DD)? ")
            employee_object.review_rating = int(input("What is their review rating (1-5)? "))
            employee_data.append(employee_object)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return employee_data
