def make_coffee(flavor="latte", size="medium"):
    """
    Simulates making a coffee with optional flavor and size.
    """
    print(f"Preparing a {size} {flavor} coffee.")

# Calling with both arguments provided (overriding defaults)
make_coffee("cappuccino", "large")
# Output: Preparing a large cappuccino coffee.

# Calling without the size argument (using the default 'medium')
make_coffee("espresso")
# Output: Preparing a medium espresso coffee.

# Calling without any arguments (using both defaults)
make_coffee()
# Output: Preparing a medium latte coffee.