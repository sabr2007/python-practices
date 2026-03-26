cust_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
discount = 0
if subtotal > 5000:
    discount = (subtotal * 10) / 100
total = subtotal - discount

print("==============================\n"
    "          SHOP RECEIPT\n"
    "==============================\n"
    f"Customer : {cust_name}\n"
    f"Product : {product_name}\n"
    f"Price : {price} KZT\n"
    f"Quantity : {quantity}\n"
    "------------------------------\n"
    f"Subtotal : {subtotal} KZT\n"
    f"Discount : {discount} KZT\n"
    f"Total : {total} KZT\n"
    "==============================" )

print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)
