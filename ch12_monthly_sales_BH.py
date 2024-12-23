import csv
import os

FILENAME = "monthly_sales.txt"


def display_menu():
    print("COMMAND MENU")
    print("view - View sales for specified month")
    print("edit - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit - Exit program")

    
def read_dictionary():

    sales_dictionary = {}
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                month, price = line.strip().split('\t')
                sales_dictionary[month] = float(price)
    except FileNotFoundError:
        print("File not found.")
    return sales_dictionary


def write_dictionary(sales_dictionary):
    with open(FILENAME, 'w') as file:
        for month, price in sales_dictionary.items():
            file.write(f"{month}\t{price}\n")

def edit_dictionary(sales_dictionary):
    month = input("Enter the month abbreviation: ")
    if month not in sales_dictionary:
        print("invalid month")
        return
    try:
        new_price = float(input("Enter the new price: "))
        sales_dictionary[month] = new_price
        write_dictionary(sales_dictionary)
        print("Updated.")
    except ValueError:
        print("Please enter number")


def view_dictionary(sales_dictionary):
    print("Monthly Sales:")
    for month, price in sales_dictionary.items():
        print(f"{month}: {price}")

def display_totals(sales_dictionary):
    total = sum(sales_dictionary.values())
    average = total / len(sales_dictionary)
    print("Yearly total: " + str(total))
    print("Monthly average: " + str(average))
                
        

def main():
    display_menu()
    sales_dictionary = read_dictionary()
    
    while True:
        command = input("Enter option choice: ")
        if command == "view":
            view_dictionary(sales_dictionary)
        elif command == "edit":
            edit_dictionary(sales_dictionary)
        elif command == "totals":
            display_totals(sales_dictionary)
        elif command == "exit":
            break


if __name__ == "__main__":
    main()

