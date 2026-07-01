
coffee = 8.50
tea = 6.00
sandwich = 12.00

def calculate_bill(coffee_qty, tea_qty, sandwich_qty):
    
    total = (coffee_qty * coffee) + (tea_qty * tea ) + (sandwich_qty * sandwich)
    return total


def print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total):
    print("===== RECEIPT =====")
    print("Customer:", customer_name)
    print("Coffee:", coffee_qty)
    print("Tea:", tea_qty)
    print("Sandwich:", sandwich_qty)
    print("-------------------")
    print("Total = RM", format(total, ".2f"))