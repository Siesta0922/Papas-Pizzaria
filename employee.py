import os
import datetime
import main_module
import random

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

def orderStock(errorMessage = ""):
    os.system('cls')
    print(errorMessage)

    try:
        choice = int(input("Order assorted stock [5-20] [0 to Exit]: "))
        if choice == 0:
            return
        elif int(choice) <= 20 and int(choice) >= 5:
            orderStock("Order Complete!\n" + getAssortedStock(int(choice)))
        else:
            orderStock("Wrong input. Try again!")
    except Exception:
        orderStock("Wrong input. Try again!")

def getAssortedStock(quantity):
    flavorCount = [0, 0, 0, 0]
    pizzas = ["Burger Pizza", "Hawaiian", "Meat Lover's", "Mushroom"]
    assortedStock = []

    for i in range(quantity):
        randomIndex = random.randint(0, len(pizzas)-1)
        assortedStock.append(pizzas[randomIndex])
        flavorCount[randomIndex] += 1

    sortedAssortedStock = mergeSort(assortedStock)

    with open("pizzastock.txt", "a") as file:
        for pizza in sortedAssortedStock:
            file.write(f"{pizza}\n")

    assortedReceipt = ""
    for i in range(0, len(flavorCount)):
        if flavorCount[i] > 0:
            assortedReceipt += f"{pizzas[i]} ({flavorCount[i]}x)\n"
    
    return assortedReceipt


def mergeSort(list):
    if len(list) > 1:
        middle = len(list)//2
        lefthalf = list[:middle]
        righthalf = list[middle:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i + 1
            else:
                list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return list
        
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

def employee_menu(username, errorMessage = ""):
    os.system('cls')
    print("Employee Menu:")
    print("1. Order Pizza for Customer")
    print("2. Order Pizza Stock")
    print("3. Exit")
    print(errorMessage)

    choice = input("Enter your choice: ")

    if choice == "1":
        order_pizza(username)
    elif choice == "2":
        orderStock()
    elif choice == "3":
        print("Goodbye!")
        main_module.main()
    else:
        employee_menu(username, "Invalid choice. Try again!")

def order_pizza(username):
    pizzas_ordered = []
    total_cost = 0
    message = ""

    pizza_stock = []
    try:
        with open("pizzastock.txt", "r") as file:
            pizza_stock = file.read().splitlines()
    except FileNotFoundError:
        input("Error: pizzastock.txt not found. Please make sure stock exists.")
        employee_menu(username)

    os.system('cls')
    customer_name = input("Enter the customer's name: ")

    while True:
        os.system('cls')
        print(f"Ordering for: {customer_name}")
        print("Pizza Menu (Stock Available):")
        
        stock_count = {pizza: pizza_stock.count(pizza) for pizza in set(pizza_stock)}
        for key, value in pizza_menu.items():
            available = stock_count.get(value["name"], 0)
            print(f"{key}. {value['name']} - ${value['price']} (Available: {available})")
        print("5. Remove Last Pizza Ordered")
        print("6. Finish ordering")
        print(message)

        pizza_choice = input("Enter your pizza choice (1-4), '5' to undo last, or '6' to finish ordering: ")

        if pizza_choice == '6':
            if len(pizzas_ordered) > 0:
                os.system('cls')
                print(f"Order Summary for {customer_name}:\n")
                for pizza in pizzas_ordered:
                    print(f"Pizza: {pizza['name']} - ${pizza['price']:.2f}")
                    total_cost += pizza['price']
                print(f"\nTotal Cost: ${total_cost:.2f}\n")
                input("Press enter to continue: ")
                
                with open("pizzastock.txt", "w") as file:
                    for pizza in pizza_stock:
                        file.write(f"{pizza}\n")

                generate_receipt(username, customer_name, pizzas_ordered)

                input("Order complete! Press enter to return to the employee menu.")
            else:
                input("No pizzas ordered. Press enter to return to the employee menu.")
            break

        elif pizza_choice == '5':
            if len(pizzas_ordered) > 0:
                last_pizza = pizzas_ordered.pop()
                pizza_stock.append(last_pizza['name'])
                message = f"Last order ({last_pizza['name']}) has been undone!"
            else:
                message = "No pizza to undo!"
        
        elif pizza_choice in pizza_menu:
            pizza_name = pizza_menu[pizza_choice]["name"]
            pizza_price = pizza_menu[pizza_choice]["price"]

            if stock_count.get(pizza_name, 0) > 0:
                message = f"You have ordered a {pizza_name} pizza for ${pizza_price}!"
                pizzas_ordered.append({"name": pizza_name, "price": pizza_price})
                pizza_stock.remove(pizza_name)
                stock_count[pizza_name] -= 1
            else:
                message = f"Sorry, {pizza_name} is out of stock."
        else:
            message = "Invalid pizza choice. Try again!"

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