def converterMachine(listName):
    i = 0
    while i <= len(listName)-1:
        sentence = str(listName[i])
        i = i+1
        if i < len(listName)-1:
            print(sentence, end=", ")
        elif i == len(listName)-1:
            print(sentence, end=" & ")
        else:
            print(sentence + '.')


message = []
tags = ["Name", "Age", "Address"]

for tag in tags:
    text = input("Enter your " + tag + ": ")
    message.append(text)

converterMachine(message)