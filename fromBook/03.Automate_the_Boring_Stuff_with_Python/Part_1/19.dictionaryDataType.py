birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} #making a list


while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "": #conditional logic
        break
    if name in birthdays.keys():
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday Database updated.")
        print(birthdays)
