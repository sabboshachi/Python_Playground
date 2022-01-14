

sandwich_orders  = ["chicken sandwich" , "chesse sandwich" , "veg sandwich" , "pastrami"]

finished_sandwich = []


while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    if sandwich_order != "pastrami":
        print("I have made " + sandwich_order.title() + ".")
        finished_sandwich.append(sandwich_order)
    else :
        print("Sorry! We are out of Pastrami. ")
print("All i made is : ")
print(finished_sandwich)