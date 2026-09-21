from database.readwrite import (read_employees)


def employee_auth(username:str, password:str):
    employees = read_employees()

    for employee in employees:
        if employee.get("username") == username:
            return employee.get("role") if employee.get("password") == password else None
    return None
