from database.readwrite import (read_report, read_products, add_product)

def admin_section():
    running = True
    while(running):
        print("=" * 50)
        print("This is admin control center")
        print("=" * 50)
        print("Enter the number of the corresponding to the action.")
        print("1. Check report")
        print("2. Restock")
        print("3. Add new items")
        print("4. Remove items")
        print("5. Exit")
        
        action = int(input("Select one of the actions: "))
        match action:
            case 1:
                check_report()
            case 2:
                restock()
            case 3:
                add_items()
            case 4:
                remove_items()
            case 5:
                running = False
                return True


def check_report():
    print("=" * 50)
    username = input("Enter employee name: ")
    reports = read_report()
    found_report = False
    for report in reports:
        if report.get("author") == username:
            found_report = True
            print(f"Report from {username} **{report.get("message")}**")

    if not found_report:
        print(f"There is not report from {username}")
    print("=" * 50)


def restock():
    pass


def add_items():
    pass


def remove_items():
    pass


if __name__ == "__main__":
    admin_section("ben")