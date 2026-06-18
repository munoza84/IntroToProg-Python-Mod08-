# Assignment 08 — Employee Ratings Application

**Author:** Alex Munoz  
**Date:** June 12, 2026  
**Course:** Foundations of Programming: Python

---

## Overview

This application extends Assignment 07 by splitting a single-file Python program into a layered,
multi-file architecture. Employee review data is collected, displayed, and persisted to a JSON file.
Each layer — data, processing, and presentation — lives in its own module, making the code easier
to read, test, and maintain independently.

---

## File Structure

```
Assignment08/
├── data_classes.py              # Person and Employee data classes
├── processing_classes.py        # FileProcessor — reads/writes JSON
├── presentation_classes.py      # IO — all user input and output
├── main.py                      # Entry point — constants, variables, main loop
├── EmployeeRatings.json         # Persistent data store
├── test_data_classes.py         # Unit tests for Person and Employee
├── test_processing_classes.py   # Unit tests for FileProcessor
└── test_presentation_classes.py # Unit tests for IO
```

---

## How to Run

```bash
cd Assignment08
python main.py
```

To run all unit tests:

```bash
python -m unittest discover -v
```

---

## Menu

```
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
```

---

## Classes

### `Person` — `data_classes.py`

Base class representing a person with a first and last name.

| Member | Type | Description |
|---|---|---|
| `first_name` | `str` | Letters only; stored and returned in title case. Defaults to `""`. |
| `last_name` | `str` | Letters only; stored and returned in title case. Defaults to `""`. |
| `__str__()` | method | Returns `"FirstName,LastName"` |

Validation: both setters reject values containing non-letter characters and raise `ValueError`.

---

### `Employee(Person)` — `data_classes.py`

Inherits from `Person` and adds two review fields.

| Member | Type | Description |
|---|---|---|
| `review_date` | `str` | Must be a valid `YYYY-MM-DD` date. Defaults to `"1900-01-01"`. |
| `review_rating` | `int` | Must be `1`, `2`, `3`, `4`, or `5`. Defaults to `3`. |
| `__str__()` | method | Returns `"FirstName,LastName,ReviewDate,ReviewRating"` |

Validation:
- `review_date` setter calls `datetime.date.fromisoformat()` and raises `ValueError` on a bad format.
- `review_rating` setter checks membership in `(1, 2, 3, 4, 5)` and raises `ValueError` otherwise.

---

### `FileProcessor` — `processing_classes.py`

Handles reading and writing `EmployeeRatings.json`. All methods use `@staticmethod`.

#### `read_employee_data_from_file(file_name, employee_data, employee_type)`

- Opens the JSON file and converts each dictionary row into an `Employee` object.
- `employee_type` is passed as a parameter (rather than hard-coded) so the function works with any subclass.
- Raises `FileNotFoundError` if the file does not exist.

#### `write_employee_data_to_file(file_name, employee_data)`

- Converts each `Employee` object to a dictionary and writes the list to the JSON file with `indent=2`.
- Raises `TypeError`, `PermissionError`, or a generic `Exception` depending on failure type.

---

### `IO` — `presentation_classes.py`

Manages all user interaction. All methods use `@staticmethod`.

| Method | Description |
|---|---|
| `output_error_messages(message, error=None)` | Prints a custom message; optionally prints technical exception details. |
| `output_menu(menu)` | Prints the menu string with surrounding blank lines. |
| `input_menu_choice()` | Prompts for a choice; raises `Exception` if not `1`–`4`. |
| `output_employee_data(employee_data)` | Prints each employee with their rating label (see table below). |
| `input_employee_data(employee_data, employee_type)` | Collects and validates all four fields; appends a new `Employee` to the list. |

**Rating labels:**

| Rating | Label |
|---|---|
| 5 | Leading |
| 4 | Strong |
| 3 | Solid |
| 2 | Building |
| 1 | Not Meeting Expectations |

---

## Data File — `EmployeeRatings.json`

```json
[
  {
    "FirstName": "Alice",
    "LastName": "Johnson",
    "ReviewDate": "2024-01-15",
    "ReviewRating": 5
  },
  {
    "FirstName": "Bob",
    "LastName": "Smith",
    "ReviewDate": "2024-03-20",
    "ReviewRating": 3
  }
]
```

The file must exist before running the application. At least one record is required to avoid a startup error.

---

## Error Handling

All exceptions are routed through `IO.output_error_messages()`. Structured handling covers:

- File not found on startup
- Non-letter characters in first or last name
- Invalid date format (not `YYYY-MM-DD`)
- Review rating outside `1`–`5`
- File write failures (permission or type errors)

---

## Unit Tests

| File | Test Class | Tests |
|---|---|---|
| `test_data_classes.py` | `TestPerson`, `TestEmployee` | 17 |
| `test_processing_classes.py` | `TestFileProcessor` | 9 |
| `test_presentation_classes.py` | `TestIO` | 13 |
| | **Total** | **39** |

Tests use `unittest.mock.patch` to intercept `builtins.input` and `sys.stdout`, allowing all
input/output to be verified without manual interaction. `setUp()` and `tearDown()` methods in
`TestFileProcessor` create and remove a temporary JSON file for each test.

---

## Constants

```python
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
```

## Variables

```python
employees: list = []  # list of Employee objects
menu_choice = ''
```
