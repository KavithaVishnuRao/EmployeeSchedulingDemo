from ortools.sat.python import cp_model
from datetime import datetime
import json
from utils.db_utils import update_shifts

def parse_time(date_str, time_str):
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

def schedule_employees(employees, shifts, db_path):
    model = cp_model.CpModel()
    assignments = {}
    

    # Precompute shift durations in hours
    duration_hours_map = {}
    for shift_id, date, start, end, role, assignedempid in shifts:
        start_dt = parse_time(date, start)
        end_dt = parse_time(date, end)
        duration = (end_dt - start_dt).seconds // 3600
        duration_hours_map[shift_id] = duration

    # Create assignment variables with availability and role constraints
    for shift_id, date, start, end, role,assignedempid in shifts:
        for emp in employees:
            key = (shift_id, emp.employee_id)
            assignments[key] = model.NewBoolVar(f'shift_{shift_id}_emp_{emp.employee_id}')
            shift_day = parse_time(date, start).strftime("%a")  # e.g., "Tue"
            #shift_hour = parse_time(date, start).hour
            availability_str = ''.join(emp.availability)
            availability =json.loads(availability_str)
            # if role != emp.role or shift_day not in availability or not (availability[shift_day][0] <= shift_hour < availability[shift_day][1]):
            #      model.Add(assignments[key] == 0)
            availability = json.loads(emp.availability)
            shift_start_hour = parse_time(date, start).hour
            shift_end_hour = parse_time(date, end).hour

            if role != emp.role or shift_day not in availability:
                model.Add(assignments[key] == 0)
                #print(f"{emp.name} cant shift {role}  shiftid {shift_id}")
            else:
                available_start, available_end = availability[shift_day]
                if not (available_start <= shift_start_hour and shift_end_hour <= available_end):
                    model.Add(assignments[key] == 0)
                #else:
                    # print(f"{emp.name} CAN take shift {shift_id}")




    # Constraint: One employee per shift
    for shift_id, *_ in shifts:
        model.Add(sum(assignments[(shift_id, emp.employee_id)] for emp in employees) == 1)

    # Constraint: Max hours per employee
    for emp in employees:
        emp_hours = sum(
            assignments[(sid, emp.employee_id)] * duration_hours_map[sid]
            for sid, *_ in shifts
        )
        model.Add(emp_hours <= emp.max_hours)
    model.Maximize(sum(assignments.values()))

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        update_shifts(db_path,assignments,solver)
        for key, var in assignments.items():
            if solver.Value(var):
                shift_id, emp_id = key
                print(f"Assign Employee {emp_id} to Shift {shift_id}")
    else:
        print("No optimal schedule found.")