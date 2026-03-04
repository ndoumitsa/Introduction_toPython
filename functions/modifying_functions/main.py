# 1. Apply a discount (default 5%)
def apply_discount(price, discount=0.05):
    return price * (1 - discount)

# 2. Apply tax (default 7%)
def apply_tax(price, tax=0.07):
    return price * (1 + tax)

# 3. Calculate total by chaining discount then tax
def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    return apply_tax(discounted, tax)

# 4. Default values
total_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_default}")

# 5. Custom keyword arguments
total_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_custom}")