
age = input("Please Enter your age:")
age = int (age)

if age < 4:
    print("Your admisson cost is $0")
elif age < 18:
    print("Your addmission cost is $5")
elif age < 65:
    print("Your admission cost is $10")
elif age >= 65:
    print("Your admission cost is $5")

