import os
import main_module

admin_database = {
    "admin": "password"
}

errorMessage = ""
def login_admin():
    global errorMessage; print(errorMessage)
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in admin_database and password == admin_database[username]:
        os.system('cls'); input("Login successful!\nPlease enter to continue: ")
        admin_menu()
    else:
        errorMessage = "Invalid username or password. Try again!"

def admin_menu():
    os.system('cls')
    print("Admin Menu:")
    print("1. View Employee Logs")
    print("2. View Receipts")
    print("3. Exit")
    global errorMessage; print(errorMessage)
    choice = input("Enter your choice: ")

    if choice == "1":
        view_employee_logs()
    elif choice == "2":
        view_receipts()
    elif choice == "3":
        print("Goodbye!")
        main_module.main()
    else:
        errorMessage = "Invalid choice. Try again!"
        admin_menu()

def view_employee_logs():
    os.system('cls')
    print("Employee Logs:")
    for filename in os.listdir():
        if filename.endswith("employeelog.txt"):
            print(filename)
            with open(filename, "r") as file:
                content = file.read()
                print(content)
    input("Press enter to return: ")
    admin_menu()

def view_receipts():
    os.system('cls')
    print("Receipts:")
    for filename in os.listdir():
        if filename.endswith("receipt.txt"):
            print(filename)
            with open(filename, "r") as file:
                content = file.read()
                print(content)
    input("Press enter to return: ")
    admin_menu()

def main():
    while True:
        os.system('cls'); print("Admin Login")
        login_admin()

if __name__ == "__main__":
    main()