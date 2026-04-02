customer = input("Enter customer name: ")
subtotal = 0
count = 0
while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter price: "))
    subtotal += price
    count += 1
print("Customer :", customer.upper())
print("Items :", count)
print("Subtotal :", subtotal, "KZT")


hour = int(input("Enter current hour (0-23): "))
print("-" * 30)
if 6 <= hour < 12:
    discount = subtotal * 0.10
    label = "Morning discount"
elif 12 <= hour < 17:
    discount = 0
    label = "No discount"
elif 17 <= hour < 22:
    discount = subtotal * 0.05
    label = "Evening discount"
else:
    print("Closed")
    exit()
total_after_discount = subtotal - discount
tip = total_after_discount * 0.10
total = total_after_discount + tip

print("Time period :", label)
print("Discount :", discount, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total :", total, "KZT")
print("-" * 30)



print("Name uppercase :", customer.upper())
print("Name lowercase :", customer.lower())
print("Name length :", len(customer))

if customer[0].upper() == 'A' or customer[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")