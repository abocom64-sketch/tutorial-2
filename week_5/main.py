from utils import calculate_bill, print_receipt

customer_name = input("Customer name: ")

coffee_qty = int(input("Coffee quantity: "))
tea_qty = int(input("Tea quantity: "))
sandwich_qty = int(input("Sandwich quantity: "))


total = calculate_bill(coffee_qty, tea_qty, sandwich_qty)

print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total)
