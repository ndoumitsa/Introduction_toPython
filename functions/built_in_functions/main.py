# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, values in products.items():
    # unpack price (string) and quantity (string)
    price = float(values[0])
    quantity_sold = int(values[1])

    # compute and report total sales
    total_sales = price * quantity_sold
    print(f"Total sales for {product}: ${total_sales}")
    
    # add each total_sales to the list
    total_sales_list.append(total_sales)

# calculate and print summary statistics
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"\nTotal sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")