
# Student Attendance System

## Overview
This project is a Python-based attendance tracking system that processes and analyzes attendance data for a class. It provides functionality to check attendance, identify late students, track sign-in and sign-out times, and find students who did not attend. The program uses predefined roster and attendance data for testing.

## Features

### Attendance Data Handling
- **Roster Management**:
  - Maintains a list of enrolled students.
- **Attendance Tracking**:
  - Processes attendance records with timestamps for sign-in and sign-out.

### Attendance Queries
- Identify students who did not attend class.
- List all sign-in and sign-out times for a specific student.
- Retrieve the first student to enter the class.
- Find students who arrived late.

### Reporting
- Generate attendance reports for all students, including late arrivals and absentees.
- Display attendance times for all students.

## Files

### Source Files
1. **`dataEntry.py`**:
   - Contains functions to populate the roster and attendance data for testing purposes:
     - `fill_roster`: Returns a list of students enrolled in the class.
     - `fill_attendance_data`: Returns a list of attendance records with timestamps.

2. **`p1.py`**:
   - Implements the main program logic, including attendance queries and reporting functions:
     - `list_students_not_in_class`: Identifies students absent from class.
     - `list_all_times_checking_in_and_out`: Lists all sign-in and sign-out times for a specific student.
     - `list_all_times_checked_in`: Returns the first sign-in time for all students.
     - `list_students_late_to_class`: Identifies students who arrived late.
     - `get_first_student_to_enter`: Finds the first student to sign in.

### Data Files
- Roster and attendance data are generated internally for testing.

## Installation

1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed on your system.

## Usage

1. Run the program:
   ```bash
   python3 p1.py
   ```
2. Follow the prompts to generate attendance reports or query specific data.

### Example Functions

#### List Students Not in Class
```python
absent_students = list_students_not_in_class(classRoster, attendData)
print(absent_students)
```

#### List Sign-In and Sign-Out Times for a Student
```python
times = list_all_times_checking_in_and_out("Lupoli, Shawn", attendData)
print(times)
```

#### Find First Student to Enter
```python
first_student = get_first_student_to_enter(attendData)
print(first_student)
```

#### Identify Late Students
```python
late_students = list_students_late_to_class(attendData)
print(late_students)
```

## Dependencies
- Python 3.x

## Authors
- **Ashraf Kawooya**
- **Date**: 11/3/2022
- **Lab Section**: 11
- **Email**: ashrafk1@umbc.edu

## License
This project is for educational purposes and does not include warranties or guarantees.
