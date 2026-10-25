from authentication.auth import employee_auth
from admin import admin_section
from employee import employee_section


running = True

while(running):
    print("=" * 50)
    print(f"        Welcome to Cambodia's warehouse")
    print("=" * 50)
    print("Choose an option:\n0. Exit the system\n1. Continue to login")
    choice = int(input("Enter choice: "))
    match choice:
        case 0:
            running = False
            break
        case 1:
            pass

    print("*" * 50)
    print("Please enter your credential to login to the system")
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()

    credential_auth = employee_auth(username, password)
    if credential_auth:
        print(f"Welcome Mr/Mrs {username.title()}. ROLE: {credential_auth}")
    print("*" * 50)
    match credential_auth:
        case "admin":
            running = admin_section(username)
        case "employee":
            running = employee_section(username)