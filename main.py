from authentication.auth import employee_auth
from admin import admin_section
from employee import employee_section


running = True

while(running):
    print("=" * 50)
    print(f"        Welcome to Cambodia's warehouse")
    print("=" * 50)
    print("Choose an option:\n1. Continue to login\n2. Exit the system")
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            pass
        case 2:
            running = False
            break
    print("*" * 50)
    print("Please enter your credential to login to the system")
    username = input("Enter username: ").strip().title()
    password = input("Enter password: ").strip()

    credential_auth = employee_auth(username, password)
    if credential_auth:
        print(f"Welcome Mr/Mrs {username}. ROLE: {credential_auth}")
    print("*" * 50)
    match credential_auth:
        case "admin":
            running = admin_section()
        case "employee":
            running = employee_section(username)