import sqlite3
from models.employee import Employee

def get_employees(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return [Employee(*row) for row in rows]

def get_shifts(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shifts")
    shifts = cursor.fetchall()
    conn.close()
    return shifts

def update_shifts(db_path,assignments,solver):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Loop through assignments and update AssignedEmpId
    for (shift_id, employee_id), var in assignments.items():
        if solver.Value(var):
            cursor.execute("""
                UPDATE shifts
                SET AssignedEmpId = ?
                WHERE Id = ?
            """, (employee_id, shift_id))

    # Commit changes
    conn.commit()
    conn.close()
