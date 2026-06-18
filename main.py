# ------------------------------------------------------------------------------------------ #
# Title: Assignment08 - Main
# Desc: Employee Ratings application entry point using layered architecture
# Change Log: (Who, When, What)
# Alex Munoz, 2026-06-12, Created Script
# ------------------------------------------------------------------------------------------ #
from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Data -------------------------------------------- #
FILE_NAME: str = "EmployeeRatings.json"

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []
menu_choice = ''

# When the program starts, read the file data into a list of Employee objects
try:
    employees = FileProcessor.read_employee_data_from_file(
        file_name=FILE_NAME,
        employee_data=employees,
        employee_type=Employee
    )
except Exception as e:
    IO.output_error_messages("Error reading data from file.", e)

# Present and Process the data
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.output_employee_data(employee_data=employees)
        continue

    elif menu_choice == "2":
        employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
        continue

    elif menu_choice == "3":
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages("Error saving data to file.", e)
        continue

    elif menu_choice == "4":
        break

print("Program Ended")
