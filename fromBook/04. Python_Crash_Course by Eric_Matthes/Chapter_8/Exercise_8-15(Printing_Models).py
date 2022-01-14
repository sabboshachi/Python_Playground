from printing_functions import favourite_food as ff
while True:

    p_name = input("Enter your name : ")
    f_food = input("Enter your favourite food : ")

    if p_name != "quit":

        profile_1 = ff(p_name,f_food)
        print(profile_1)
    else:
        break
