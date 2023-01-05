
prompt = "Add some toppings for your pizza: "
prompt = input(prompt)
while True:

    if prompt == "quit":
        print("Your pizza is getting ready!")
        break
    else:

        prompt = input("Anything else: ")


