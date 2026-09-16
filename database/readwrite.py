from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
EMPLOYEES_FILE = BASE_DIR / "employees.json"
PRODUCTS_FILE = BASE_DIR / "products.json"


def read_json_file(path: Path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"⚠️ File not found: {path}")
    except json.JSONDecodeError:
        print(f"⚠️ File is not valid JSON (corrupted or empty): {path}")
    except PermissionError:
        print(f"⚠️ Permission denied reading file: {path}")
    except IsADirectoryError:
        print(f"⚠️ Expected a file but found a directory: {path}")
    except OSError as e:
        print(f"⚠️ OS error while reading file: {e}")


def write_json_file(path: Path, data):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except PermissionError:
        print(f"⚠️ Permission denied writing to file: {path}")
    except IsADirectoryError:
        print(f"⚠️ Expected a file but found a directory: {path}")
    except FileNotFoundError:
        print(f"⚠️ Directory does not exist for path: {path}")
    except TypeError as e:
        print(f"⚠️ Data could not be serialized to JSON: {e}")
    except OSError as e:
        print(f"⚠️ OS error while writing file: {e}")


def read_employees():
    return read_json_file(EMPLOYEES_FILE) or []


def read_products():
    return read_json_file(PRODUCTS_FILE) or []


def add_product(new_product: dict):
    products = read_products()
    products.append(new_product)
    if write_json_file(PRODUCTS_FILE, products):
        return "Product added successfully."
    return "Failed to add product."
