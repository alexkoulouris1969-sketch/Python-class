def coffee_price_checker():
    # Dictionary storing beverages and their prices
    menu = {
        "espresso": 2.0,
        "dopio": 2.4,
        "lungo": 3.0,
        "cappuccino": 3.2,
        "latte": 3.4,
        "flat white": 3.8,
        "americano": 2.8,
        "cold brew": 4.0
    }
    # Display available options
    print("--- Coffee Shop Menu ---")
    for item in menu:
        print(f"- {item.title()}")
        # Get user input, strip whitespace, and convert to lowercase for matching
    choice = input("Enter the beverage you want: ")
            