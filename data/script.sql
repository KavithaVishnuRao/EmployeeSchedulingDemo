CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    max_hours_per_week INTEGER,
    availability TEXT  -- e.g., "Mon AM, Tue PM, Wed AM"
)
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    max_hours_per_week INTEGER,
    availability TEXT  -- e.g., "Mon AM, Tue PM, Wed AM"
)



--insert data

INSERT INTO employees (employee_id, name, role, max_hours, availability) VALUES
(1, 'Alice', 'Cashier', 40, '{"Fri": [9, 17], "Sat": [9, 17]}'),
(2, 'Bob', 'Manager', 40, '{"Fri": [8, 16], "Sat": [8, 16]}'),
(3, 'Clara', 'Stocker', 40, '{"Fri": [10, 18], "Sat": [10, 18]}');

INSERT INTO shifts (id, date, start_time, end_time, required_role) VALUES
(101, '2025-08-15', '09:00', '13:00', 'Cashier'),   -- Friday
(102, '2025-08-15', '08:00', '12:00', 'Manager'),   -- Friday
(103, '2025-08-15', '10:00', '14:00', 'Stocker'),   -- Friday
(104, '2025-08-16', '09:00', '13:00', 'Cashier'),   -- Saturday
(105, '2025-08-16', '08:00', '12:00', 'Manager'),   -- Saturday
(106, '2025-08-16', '10:00', '14:00', 'Stocker');   -- Saturday
