import csv
import sys

items = [
    {"Name":"Milk", "Quantity": 120.111, "Unit": "l", "Unit Price (PLN)": 2.3},
    {"Name":"Sugar", "Quantity": 1000, "Unit": "kg", "Unit Price (PLN)": 3},
    {"Name":"Flour", "Quantity": 12000, "Unit": "kg", "Unit Price (PLN)": 1.2},
    {"Name":"Coffee", "Quantity": 25, "Unit": "kg", "Unit Price (PLN)": 40}
]

sold_items = [    
    {"Name":"Milk", "Quantity": 0, "Unit": "l", "Unit Price (PLN)": 2.3},
    {"Name":"Sugar", "Quantity": 0, "Unit": "kg", "Unit Price (PLN)": 3},
    {"Name":"Flour", "Quantity": 0, "Unit": "kg", "Unit Price (PLN)": 1.2},
    {"Name":"Coffee", "Quantity": 0, "Unit": "kg", "Unit Price (PLN)": 40}]

def get_items(items):
    print("{:<10s}{:>9s}{:>12s}{:>23s}".format("Name","Quantity","Unit","Unit Price (PLN)"))
    dash = "-" * 55
    print(dash)
    for i in range(len(items)):
        print("{:<10s}{:>9.2f}{:>12s}{:>14.2f}".format(list(items[i].values())[0],list(items[i].values())[1],list(items[i].values())[2],list(items[i].values())[3]))

def add_item(items):
    print("Adding to warhouse...")
    name = str(input("Item name: ")) 
    quantity = int(input("Quantity: "))
    unit_name = str(input("Unit name: "))
    unit_price = float(input("Unit Price: "))
    items.append({"Name":name, "Quantity": quantity, "Unit": unit_name, "Unit Price (PLN)": unit_price})
    get_items(items)

def sell_item(items, sold_items):
    name = str(input("Item name: "))
    quantity_to_sell = int(input("Quantity to sell: "))
    for i in range(len(items)):
        if items[i]["Name"] == name:
            items[i]["Quantity"] = items[i]["Quantity"] - quantity_to_sell           
            for z in range(len(sold_items)):
                if sold_items[z]["Name"] == name:
                    sold_items[z]["Quantity"] = sold_items[z]["Quantity"] + quantity_to_sell
            
    #print(sold_items)
    get_items(items)

def get_costs(items):
    costs = round(sum([items[i]["Quantity"] * items[i]["Unit Price (PLN)"] for i in range(len(items))]), 2)
    return costs

def get_income(sold_items):
    income = round(sum([sold_items[i]["Quantity"] * sold_items[i]["Unit Price (PLN)"] for i in range(len(sold_items))]), 2)
    return income

def show_revenue(costs, income):
    print("Revenue break down (PLN): ")
    print(f"Income: {income}")
    print(f"Costs: {costs}")
    print("-" * 10)
    print(f"Revenue: {income - costs}")

def export_items_to_csv(items):
    with open("c:\\Users\\admin\Desktop\Projekt Magazyn\magazyn.csv", "w") as new_file:
        fieldname = ["Name", "Quantity", "Unit", "Unit Price (PLN)"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldname, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        for line in items:
            csv_writer.writerow(line)

def load_items_from_csv(items):
    items.clear()
    infile = sys.argv[1]
    with open(infile, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for line in csv_reader:
            items.append(line)

def menu(items):
    message = print("What would you like to do? (for commands write commands): ")
    commands = "show, exit, add, sell, show revenue, save"
    command = input().lower()
    if command == "exit":
        print("Exiting.... Bye!!")
        exit(1)
    elif command == "show":
        get_items(items)
    elif command == "add":
        add_item(items)
    elif command == "sell":
        sell_item(items, sold_items)
    elif command == "show revenue":
        costs = get_costs(items)
        income = get_income(sold_items)
        show_revenue(costs, income)
    elif command == "commands":
        print(commands)
    elif command == "save":
        export_items_to_csv(items)
    elif command == "load":
        load_items_from_csv(items)
    return message


if __name__ == "__main__":
    load_items_from_csv(items)
    while True:
        menu(items)
        
