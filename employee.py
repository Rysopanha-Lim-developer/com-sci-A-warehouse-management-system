from database.readwrite import (read_products, write_report)
from admin import (check_stock)

def employee_section(username: str):
    if not username:
        username = input("Enter username for testing: ").strip().title()
    
    running = True
    while (running):
        print("-" * 50)
        print(f"Welcome {username.title()}")
        print("This is employees center")
        print("=" * 50)
        print("Enter the number of the corresponding to the action.")
        print("0. To exit")
        print("1. Check Stock")
        print("2. Write Report")

        action = int(input("Select one of the actions: "))
        match action:
            case 0:
                running = False
                return True
            case 1:
                check_stock()
            case 2:
                employee_report(username)

def employee_report(username:str):
    status = input("Follow the format DATE/MONTH/YEAR (or 0 to cancel)\nEnter date: ").strip()
    if status == "0":
        print("Report Cancelled.")
        return

    message = input("Enter report message (or 0 to cencel): ")
    if message == "0":
        print("Report Cancelled.")
        return
    
    new_report = {
        "author": username.lower(),
        "status": status,
        "message": message
    }
    
    result = write_report(new_report)
    print(result)

if __name__ == "__main__":
    employee_section("Heng")