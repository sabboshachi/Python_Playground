
sandwich_orders  = ["chicken sandwich" , "chesse sandwich" , "veg sandwich"]
finished_sandwich = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I have made " + sandwich_order.title() + ".")
    finished_sandwich.append(sandwich_order)
print("All i made is : ")
print(finished_sandwich)