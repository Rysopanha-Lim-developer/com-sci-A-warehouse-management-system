# Warehouse Management System

A Python-based, command-line Warehouse Management System developed as a computer science project. The application provides role-based access for administrators and employees to manage inventory, check stock levels, and handle employee reports.

## Features

### Administrator
- View employee reports.
- Check product stock by category.
- Identify products that need restocking.
- Restock existing products.
- Add new products to the inventory.
- Remove products from the inventory.

### Employee
- Log in using employee credentials.
- View product stock by category.
- Submit reports to the administrator.

### Data Storage
- Store employee account information in JSON files.
- Store product inventory and stock quantities in JSON files.
- Store employee reports in JSON files.
- Preserve data between application runs through file-based storage.

## Requirements

- Python 3.10 or newer
- Git (optional, for cloning the repository)
- A terminal or command-line application

The application uses Python's built-in libraries and does not require a separate database server.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rysopanha-Lim-developer/com-sci-A-warehouse-management-system.git
```

### 2. Navigate to the project directory

```bash
cd com-sci-A-warehouse-management-system
```

### 3. Verify Python installation

```bash
python --version
```

Make sure the installed version is Python 3.10 or newer.

On some systems, use:

```bash
python3 --version
```

## How to Run

From the project's root directory, run:

```bash
python main.py
```

Alternatively, on systems that use `python3`:

```bash
python3 main.py
```

On Windows, you can also try:

```bash
py main.py
```

## Usage

### 1. Start the application

After running `main.py`, the main menu will appear.

### 2. Log in

Select the login option and enter your credentials.

### 3. Choose your role

After successful authentication, the application displays the menu associated with your account.

**Administrator operations:**
- Check employee reports.
- Check product stock.
- Restock products.
- Add products.
- Remove products.

**Employee operations:**
- Check product stock.
- Submit employee reports.

Follow the on-screen instructions to navigate the menus and perform operations.

## Project Structure

```text
com-sci-A-warehouse-management-system/
├── authentication/
│   └── auth.py
├── database/
│   ├── readwrite.py
│   ├── employees.json
│   ├── products.json
│   └── reports.json
├── admin.py
├── employee.py
├── main.py
├── README.md
└── LICENSE
```

### Main Components

| Component | Description |
|---|---|
| `main.py` | Application entry point and main menu. |
| `admin.py` | Administrator operations for inventory management and employee reports. |
| `employee.py` | Employee operations for checking stock and submitting reports. |
| `authentication/auth.py` | Handles user authentication. |
| `database/readwrite.py` | Handles JSON data reading and writing. |
| `database/employees.json` | Stores employee account information. |
| `database/products.json` | Stores product inventory data. |
| `database/reports.json` | Stores employee reports. |

## Data Persistence

The application uses JSON files for data storage rather than a traditional database management system.

Changes made through the application are saved to the corresponding files. Avoid deleting or manually modifying these files unless you understand their expected data structure.

## Troubleshooting

**Python is not recognized**

Make sure Python is installed and available in your system's PATH. On Windows, try running `py main.py`.

**The application cannot find a file**

Make sure you run the application from the project's root directory and that the required files are present.

**Login fails**

Verify that the credentials correspond to an existing account in the employee data file.

## Security Notice

This project is intended for educational purposes. Avoid using real passwords or sensitive business information.

## License

See the `LICENSE` file in the repository for licensing information.