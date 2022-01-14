

def favourite_food(name, food):
    """Here I'm trying to solve the problem with dictionary"""
    profile = {"Namwe" : name , "Food" : food}
    return profile

while True:

    p_name = input("Enter your name : ")
    f_food = input("Enter your favourite food : ")

    if p_name != "quit":

        profile_1 = favourite_food(p_name,f_food)
        print(profile_1)
    else:
        break
