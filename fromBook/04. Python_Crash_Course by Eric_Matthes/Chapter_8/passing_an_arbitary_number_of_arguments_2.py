def make_pizza(*toppings):
    """Summarize the pizza we are about to make """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("\t-- "+topping)







make_pizza("pepperoni")
make_pizza("mushroom", "pepperoni", "chesse")