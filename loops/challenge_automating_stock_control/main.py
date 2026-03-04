
inventory = {
    "Bread": [30, 50, 10, False],   
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item_name, data in inventory.items():
    current_stock, min_stock, restock_amount, on_sale = data
    
    print(f"Processing {item_name}")
    
    # restock until at or above minimum
    while current_stock < min_stock:
        current_stock += restock_amount
    # update stock in the dictionary
    inventory[item_name][0] = current_stock
    
    # apply discount if above threshold and not already on sale
    if current_stock > discount_threshold and not on_sale:
        inventory[item_name][3] = True

print("Processing completed")