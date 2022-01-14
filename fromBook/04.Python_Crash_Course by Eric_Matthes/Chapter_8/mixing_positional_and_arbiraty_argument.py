def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) + " Pizza with :")
    for topping in toppings:
        print("\t--" + topping)

make_pizza(12, "pepperoni")
make_pizza(15, "pepperoni", "chesse", "mushroom")
