responses = {}

#set a flag  to indicate that polling is active

polling_active = True

while polling_active:
    #prompt for the persons name and response
    name = input("\nWhat is your name : ")
    response = input("Which mountain would you like to climb someday: ")

    #store the response in the dictionary
    responses[name] = response

    #find out if anyone else is going to take the poll
    repeat = input("\nWould you like to let another persons response? : (yes/no)")
    if repeat == "no":
        polling_active = False

    #polling is complete Show results

print("\n__Poll Result__")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
