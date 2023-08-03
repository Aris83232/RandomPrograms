items = []
prices = []
quantity = []
total = 0

while True:
    item = input("\nEnter name of the item (q to quit): ")
    if item.lower() == 'q':
        break
    else:
        count = int(input(f"Enter the quantity of {item}: "))
        price = float(input(f"Enter the price of {item}: $"))
        items.append(item)
        quantity.append(count)
        prices.append(price)

print("\n-------- BILL ----------------------")
print("Item Name - Quantity - Price - Total Price")
for x in range(len(items)):
    print(f"{items[x]} - {quantity[x]} - ${prices[x]}/piece - ${quantity[x] * prices[x]}")
    total += quantity[x] * prices[x]
print("------------------------------------")
print(f"Your total bill amount is: ${total}")
print("------------------------------------")
