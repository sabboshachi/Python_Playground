# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
# with and inserted before the last item.
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.

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

spam = ["apples", "bananas", "tofu", "cats"]
converterMachine(spam)