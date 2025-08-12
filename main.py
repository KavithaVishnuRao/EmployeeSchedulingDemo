from utils.db_utils import get_employees, get_shifts
from scheduler.optimizer import schedule_employees

DB_PATH = 'data/employees.db'

employees = get_employees(DB_PATH)
shifts = get_shifts(DB_PATH)

schedule_employees(employees, shifts,DB_PATH)