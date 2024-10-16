import os
import admin
import employee


errorMessage = ""
def main():
    os.system('cls')
    print("Welcome to the Papas Pizzeria Login System!")
    print("Please choose which login system to access:")

    print("1. Employee Login")
    print("2. Admin Login")
    print("3. Exit")
    global errorMessage; print(errorMessage)

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        employee.main()
    elif choice == "2":
        admin.main()
    elif choice == "3":
        os.system('cls')
        print("Goodbye!")
        exit()
    else:
        errorMessage = "Invalid choice. Please try again!"
        main()

if __name__ == "__main__":
    main()