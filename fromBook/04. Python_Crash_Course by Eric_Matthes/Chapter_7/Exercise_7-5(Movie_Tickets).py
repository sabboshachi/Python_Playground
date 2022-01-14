
age = " "

while True:

    if age != "quit":
        age = input("Please enter your age : ")
        age = int(age)
        if age <= 3:
            print("Your ticket fair is 0$")
        elif age <= 12:
            print("Your ticket fair is 10$")
        else:
            print("Your ticket fair is 15$")
