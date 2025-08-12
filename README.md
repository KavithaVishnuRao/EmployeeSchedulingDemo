# 🧠 Employee Scheduling with Python & OR-Tools

This project uses **constraint programming** via [Google OR-Tools](https://developers.google.com/optimization) to automatically assign employees to shifts based on their **availability**, **roles**, and **hour limits**.

## 📌 Problem Overview

The goal is to generate an optimal weekly schedule that:

- Assigns employees to shifts only if they are available
- Matches employees to shifts requiring their role
- Respects each employee’s maximum allowed working hours
- Ensures each shift is covered by exactly one employee

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** SQlite
- **Solver:** Google OR-Tools (CP-SAT Solver)
- **Data Format:** JSON for availability


## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/KavithaVishnuRao/EmployeeSchedulingDemo.git
```
```bash
# Navigate into the project folder
cd EmployeeSchedulingDemo
```
```bash
# Install dependencies
pip install ortools
```

##  📋Data Model
data/script.sql : Create and insert statements. 
### 👩‍💼 Employees
Each employee has:
- employee_id: Unique identifier
- name: Full name
- role: Job role (e.g., Cashier, Manager)
- max_hours_per_week: Max hours allowed per week
- availability: JSON string mapping weekdays to available time ranges
Example:
```json
{
  "Tue": [13, 18],
  "Wed": [13, 18],
  "Thu": [13, 18]
}
```
### 🕒 Shifts
Each shift includes:
- id: Unique identifier
- date: Date of the shift (YYYY-MM-DD)
- start_time: Start time (24-hour format)
- end_time: End time (24-hour format)
- required_role: Role required for the shift
- AssignedEmpId : Foreign key referencing Employee table Id field. Updated on schedule generation.

## 🧠 Scheduling Logic
The core function schedule_employees(employees, shifts, db_path):
- Creates Boolean decision variables for each employee-shift pair
- Filters out invalid assignments based on role and availability
- Adds constraints:
- One employee per shift
- Max hours per employee
- Optionally maximizes total assignments
- Solves using CpSolver and prints the final schedule
🧪 Example Output
Assign Employee 1 to Shift 101
Assign Employee 2 to Shift 102
Assign Employee 3 to Shift 103
- Update the shifts table AssignedEmpId column


## 🧰 Utilities
- parse_time(date, time_str): Converts date and time to datetime object
- Retrieve and update employee and shift data
- Debug prints to trace assignment eligibility

## 📄 License
This project is licensed under the MIT License.







