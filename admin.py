from database.readwrite import (read_report, read_products, add_product)

def admin_section():
    running = True
    while(running):
        print("=" * 50)
        print("This is admin control center")
        print("=" * 50)
        print("Enter the number of the corresponding to the action.")
        print("1. Check report")
        print("2. Check stock")
        print("3. Add new items")
        print("4. Remove items")
        print("5. Exit")
        
        action = int(input("Select one of the actions: "))
        match action:
            case 1:
                check_report()
            case 2:
                check_stock()
            case 3:
                add_items()
            case 4:
                remove_items()
            case 5:
                running = False
                return True


def check_report():
    running = True
    while(running):
        print("=" * 50)
        print("Check employee reports")
        username = input("Enter employee name or 0 to exit: ")
        if username == "0":
            running = False
            continue

        reports = read_report()
        found_report = False
        for report in reports:
            if report.get("author") == username:
                found_report = True
                print(f"Report from {username} **{report.get("message")}**")

        if not found_report:
            print(f"There is not report from {username}")
        print("=" * 50)


def check_stock():
    running = True
    while(running):
        print("=" * 50)
        print("Choose products category below")
        print("1. Produce")
        print("2. Meat & Seafood")
        print("3. Dairy")
        print("4. Bakery")
        print("5. Deli")
        print("6. Pantry / Dry Goods")
        print("7. Baking & Spices")
        print("8. Condiments & Sauces")
        print("9. Snacks")
        print("10. Beverages")
        print("11. Frozen Foods")
        print("12. Household Supplies")
        print("13. Personal Care")
        print("14. Pet Care")

        category = int(input("Select one of the category: "))

        match category:
            case 1:
                show_item_stocks(0)
            case 2:
                show_item_stocks(1)
            case 3:
                show_item_stocks(2)
            case 4:
                show_item_stocks(3)
            case 5:
                show_item_stocks(4)
            case 6:
                show_item_stocks(5)
            case 7:
                show_item_stocks(6)
            case 8:
                show_item_stocks(7)
            case 9:
                show_item_stocks(8)
            case 10:
                show_item_stocks(9)
            case 11:
                show_item_stocks(10)
            case 12:
                show_item_stocks(11)
            case 13:
                show_item_stocks(12)
            case 14:
                show_item_stocks(13)
        running = False


def restock():
    pass


def add_items():
    pass


def remove_items():
    pass


def show_item_stocks(index):
    stocks = read_products()
    items = stocks[index]["items"]
    for i in range(len(items)):
        print("-" * 50)
        print(f"Product name   :    {items[i].get("product_name")}")
        print(f"Number in stock:    {items[i].get("stock")}")
        print(f"Current price  :    {items[i].get("price")}")
        print("-" * 50)

if __name__ == "__main__":
    admin_section()