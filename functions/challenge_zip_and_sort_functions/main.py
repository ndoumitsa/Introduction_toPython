# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Task 1: Combine the three lists into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))

# Task 2: Sort the combined list by name
sorted_products = sorted(combined_list)

# Task 3: Print the sorted list of products
for name, price, qty in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {qty}")