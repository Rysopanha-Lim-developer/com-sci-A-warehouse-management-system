def admin_section(username):
    print("-" * 50)
    print("This is admin control center")
    print("=" * 50)
    print("Enter the number of the corresponding to the action.")
    print("1. Check report")
    print("2. Restock")
    print("3. Add new items")
    print("4. Remove items")

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


def check_report():
    pass


def restock():
    pass


def add_items():
    pass


def remove_items():
    pass


if __name__ == "__main__":
    admin_section()