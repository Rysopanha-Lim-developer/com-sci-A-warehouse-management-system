from database.readwrite import (read_report, read_products, add_product, write_products)


def admin_section():
    running = True
    while(running):
        print("=" * 50)
        print("This is admin control center")
        print("=" * 50)
        print("Enter the number of the corresponding to the action.")
        print("0. Exit")
        print("1. Check report")
        print("2. Check stock")
        print("3. Restock items")
        print("4. Add new items")
        print("5. Remove items")
        
        action = int(input("Select one of the actions: "))
        match action:
            case 0:
                running = False
                return True
            case 1:
                check_report()
            case 2:
                check_stock()
            case 3:
                restock()
            case 4:
                add_items()
            case 5:
                remove_items()


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
        category = categories_menu()

        match category:
            case 0:
                running = False
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


def restock():
    running = True
    while(running):
        choice = int(input("""Do you to do bulk restock?\nEnter '0' to Exit\nEnter '1' to restock products\nPlease select an option: """))
        match choice:
            case 0:
                running = False
            case 1:
                resupply_items()



def add_items():
    running = True
    while(running):
        print("*" * 50)
        print("TO ADD NEW PRODUCT")
        print("1. Choose the category")
        print("2. Enter the product name")
        print("3. Enter the amount of stock")
        print("4. Enter the sale price")
        print("*" * 50)

        category = categories_menu()
        if category == 0:
            running = False
            break

        product_name = input("Enter product name: ")
        stock = int(input("Enter the amount of stock: "))
        price = float(input("Enter the sale price: "))
        new_product = NewProduct(product_name, stock, price)
    
        match category:
            case 0:
                running = False
            case 1:
                add_product("Produce", vars(new_product))#vars() convert an instance from memory state to a dics form
            case 2:
                add_product("Meat & Seafood", vars(new_product))
            case 3:
                add_product("Dairy", vars(new_product))
            case 4:
                add_product("Bakery", vars(new_product))
            case 5:
                add_product("Deli", vars(new_product))
            case 6:
                add_product("Pantry / Dry Goods", vars(new_product))
            case 7:
                add_product("Baking & Spices", vars(new_product))
            case 8:
                add_product("Condiments & Sauces", vars(new_product))
            case 9:
                add_product("Snacks", vars(new_product))
            case 10:
                add_product("Beverages", vars(new_product))
            case 11:
                add_product("Frozen Foods", vars(new_product))
            case 12:
                add_product("Household Supplies", vars(new_product))
            case 13:
                add_product("Personal Care", vars(new_product))
            case 14:
                add_product("Pet Care", vars(new_product))


def remove_items():
    pass


def show_item_stocks(index:int):
    stocks = read_products()
    items = stocks[index]["items"]
    for i in range(len(items)):
        print("-" * 50)
        print(f"Product name   :    {items[i].get("product_name")}")
        print(f"Current stock  :    {items[i].get("stock")}")
        print(f"Current price  :    {items[i].get("price")}")
        print("-" * 50)


def resupply_items():
    MIN_ITEMS_IN_STOCK = 20
    current_stocks = read_products()
    need_restock_items = []
    print("=========================================")
    print("Products with less than 20 items in stock")
    print("=========================================")
    for i in range(len(current_stocks)):
        items = current_stocks[i]["items"]
        for j in range(len(items)):
            if items[j].get("stock") < MIN_ITEMS_IN_STOCK:
                need_restock_items.append(items[j])
                print("-" * 50)
                print(f"Product name   :    {items[j].get("product_name")}")
                print(f"Current stock  :    {items[j].get("stock")}")
                print("-" * 50)

    restock_option = int(input("""Do you to do bulk restock?\nEnter '1' to restock all products with the same amount (100 items): """))

    match restock_option:
        case 1:
            bulk_restock(current_stocks, need_restock_items)



def categories_menu():
    print("=" * 50)
    print("Choose products category below")
    print("0. To Exit")
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
    return category


def bulk_restock(current_stocks: list, need_restock_items: list):
    AMOUNT_OF_ADDED_ITEMS = 100
    if not need_restock_items:
        print("No products need restocking.")
        return

    for item in need_restock_items:
        item["stock"] +=  AMOUNT_OF_ADDED_ITEMS 

    if write_products(current_stocks):
        print(f"Restocked {len(need_restock_items)} product(s) by 100 each.")
    else:
        print("Failed to save the restocked products.")


class NewProduct:
    def __init__(self, product_name: str, stock: int, price: float):
        self.product_name = product_name
        self.stock = stock
        self.price = price


if __name__ == "__main__":
    admin_section()