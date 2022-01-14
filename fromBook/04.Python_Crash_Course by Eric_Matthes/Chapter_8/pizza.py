def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) + " Pizza with :")
    for topping in toppings:
        print("\t--" + topping)
