# Store information  about a pizza being orfered

pizza = {

    "crust" : "thick",
    "toppings" : ["mushrooms" , "chesse" , "olive" , "pepperoni"]
}

# Summarize the order

print("You ordered a " + pizza["crust"] + "-crust pizza" + " with the following toppings: ")

for topping in pizza["toppings"]:
    print("\t" + topping.title())
