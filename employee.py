import os
import datetime
import main_module

employee_database = {
    "Vitug": "1324",
    "Kean": "0000",
    "Josh": "1234"
}

pizza_menu = {
    "1": {"name": "Mushroom", "price": 10.99},
    "2": {"name": "Hawaiian", "price": 12.99},
    "3": {"name": "Meat Lover's", "price": 14.99},
    "4": {"name": "Burger Pizza", "price": 11.99}
}

errorMessage = ""
def login_employee():
    global errorMessage; print(errorMessage)
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in employee_database and password == employee_database[username]:
        os.system('cls'); input("Login successful!\nPlease enter to continue: ")
        with open("employeelog.txt", "a") as file:
            file.write(f"{username} logged in at {datetime.datetime.now()}\n")
        employee_menu(username)
    else:
        errorMessage = "Invalid username or password. Try again!"

def employee_menu(username):
    os.system('cls')
    print("Employee Menu:")
    print("1. Order Pizza")
    print("2. Exit")
    global errorMessage; print(errorMessage)

    choice = input("Enter your choice: ")

    if choice == "1":
        order_pizza(username)
    elif choice == "2":
        print("Goodbye!")
        main_module.main()
    else:
        errorMessage = "Invalid choice. Try again!"

def order_pizza(username):
    customer_name = input("Enter the customer's name: ")
    print("Pizza Menu:")
    for key, value in pizza_menu.items():
        print(f"{key}. {value['name']} - ${value['price']}")
    print(errorMessage)

    pizzas_ordered = []
    while True:
        pizza_choice = input("Enter your pizza choice (1-4), or 'done' to finish ordering: ")
        if pizza_choice.lower() == 'done':
            break
        elif pizza_choice in pizza_menu:
            pizza_name = pizza_menu[pizza_choice]["name"]
            pizza_price = pizza_menu[pizza_choice]["price"]
            print(f"You have ordered a {pizza_name} pizza for ${pizza_price}!")
            pizzas_ordered.append({"name": pizza_name, "price": pizza_price})
            errorMessage = ""
        else:
            print("Invalid pizza choice. Try again!")

    if len(pizzas_ordered) > 0:
        generate_receipt(username, customer_name, pizzas_ordered)
    else:
        print("No pizzas ordered. Returning to employee menu.")
        employee_menu(username)

def generate_receipt(username, customer_name, pizzas_ordered):
    receipt_filename = f"{username}receipt.txt"
    total_cost = 0
    try:
        with open(receipt_filename, "a") as file:
            file.write(f"\nReceipt for {customer_name}\n")
            for pizza in pizzas_ordered:
                file.write(f"Pizza: {pizza['name']}\n")
                file.write(f"Price: ${pizza['price']:.2f}\n")
                total_cost += pizza['price']
            file.write(f"Total Cost: ${total_cost:.2f}\n")
            file.write(f"Date: {datetime.datetime.now()}\n")
            print(f"Receipt generated for {customer_name}!")
    except Exception as e:
        print(f"Error generating receipt: {e}")
    employee_menu(username)

def main():
    while True:
        os.system('cls')
        print("Employee Login")
        login_employee()

if __name__ == "__main__":
    main()