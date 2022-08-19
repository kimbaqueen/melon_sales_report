# Below are not necessary - index lengths
# SALESPERSON_INDEX = 0
# INTERNET_INDEX = 1
# DORKY_LINE_LENGTH = 80

# print("*" * DORKY_LINE_LENGTH)

# changed variable f below to better descriptor 
open_orders = open("orders-by-type.txt")
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

# count amount of each type of melon sold
for l in open_orders:
    data = l.split("|")
    melon_type = data[1]
    melon_count = int(data[2])
    melon_tallies[melon_type] += melon_count

open_orders.close()

melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

total_revenue = 0

# Calculate revenue from melon tallies
for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
    print(f"We sold {melon_tallies[melon_type]:,} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")
# not needed below print ***
# print("******************************************")
# changed variable f below to better descriptor
orders_with_sales = open("orders-with-sales.txt")
sales = [0, 0]

# Print online vs salesperson sales
for line in orders_with_sales:
    d = line.split("|")
    if d[1] == "0":
        sales[0] += float(d[3])
    else:
        sales[1] += float(d[3])
print(f"Salespeople generated ${sales[1]:,.2f} in revenue.")
print(f"Internet sales generated ${sales[0]:,.2f} in revenue.")

# Print summary report for CEO code:
if sales[1] > sales[0]:
    print("Guess there's some value to those salespeople after all.")
else:
    print("Time to fire the sales team! Online sales rule all!")
orders_with_sales.close()
# not needed below ***
# print("******************************************")
