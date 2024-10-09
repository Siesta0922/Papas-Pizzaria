import os
import main_module

admin_database = {
    "admin": "password"
}

def login_admin():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in admin_database and password == admin_database[username]:
        print("Login successful!")
        admin_menu()
    else:
        print("Invalid username or password. Try again!")

def admin_menu():
    print("Admin Menu:")
    print("1. View Employee Logs")
    print("2. View Receipts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_employee_logs()
    elif choice == "2":
        view_receipts()
    elif choice == "3":
        print("Goodbye!")
        main_module.main()
    else:
        print("Invalid choice. Try again!")

def view_employee_logs():
    print("Employee Logs:")
    for filename in os.listdir():
        if filename.endswith("employeelog.txt"):
            print(filename)
            with open(filename, "r") as file:
                content = file.read()
                print(content)
    admin_menu()

def view_receipts():
    print("Receipts:")
    for filename in os.listdir():
        if filename.endswith("receipt.txt"):
            print(filename)
            with open(filename, "r") as file:
                content = file.read()
                print(content)
    admin_menu()

def main():
    while True:
        print("Admin Login")
        login_admin()

if __name__ == "__main__":
    main()