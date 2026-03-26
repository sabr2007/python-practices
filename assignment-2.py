
name = input("Enter customer name: ")

items = 0
subtotal = 0

product_name = input("Enter product name (or done to finish): ")

while product_name != "done":
    
    price = float(input("Enter price: "))
    items += 1
    subtotal += price
    product_name = input("Enter product name (or done to finish): ")

print("Customer :", name.upper())
print(f"Items : {items}")
print(f"Subtotal : {subtotal} KZT")

discount = 0

if subtotal >= 3000 and subtotal < 7000:
    discount = (subtotal * 5) / 100
elif subtotal >= 7000:
    discount = (subtotal * 15) / 100

total = subtotal - discount

print("-" * 30)
print(f"Discount tier :", ("Yes discount") if subtotal >= 3000 else ("No discount"))
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")

print(f"Name uppercase : {name.upper()}")
print(f"Name lowercase : {name.lower()}")
print(f"Name length : {len(name)}")

print("Short name") if len(name) < 5 else print("Long name")