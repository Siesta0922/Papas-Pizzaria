import admin
import employee

def main():
    print("Welcome to the Papas Pizzeria Login System!")
    print("Please choose which login system to access:")

    print("1. Employee Login")
    print("2. Admin Login")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        employee.main()
    elif choice == "2":
        admin.main()
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again!")
        main()

if __name__ == "__main__":
    main()