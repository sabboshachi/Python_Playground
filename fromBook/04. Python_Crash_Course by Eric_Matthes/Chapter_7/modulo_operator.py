
number = input("Enter a number, and I'll tell you if it's even of odd:")
number = int(number)

if number % 2 == 0:
    print("The given number " + str(number) + " is Even!")
else:
    print("The given number " + str(number) + " is Odd!")