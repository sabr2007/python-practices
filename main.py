cust_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
discount = 0
is_discount = False
if subtotal > 5000:
    discount = (subtotal * 10) / 100
    is_discount = True
total = subtotal - discount

print("==============================\n"
    "          SHOP RECEIPT\n"
    "==============================\n"
    f"Customer: {cust_name}\n"
    f"Product: {product_name}\n"
    f"Price: {price} KZT\n"
    f"Quantity: {quantity}\n"
    "------------------------------\n"
    f"Subtotal: {subtotal} KZT\n"
    f"Discount: {discount} KZT\n"
    f"Total: {total}\n"
    "==============================" )

print(f"Discount applied: {is_discount}")
if total > 3000:
    print("Paid more than 3000: True")
else:
    print("Paid more than 3000: False")