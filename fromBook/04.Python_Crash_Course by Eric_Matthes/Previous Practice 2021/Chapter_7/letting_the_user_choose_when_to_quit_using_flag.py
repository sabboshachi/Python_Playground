prompt = "\nTell me something, and I will repaet it back to you: "
prompt += "\nEnter 'Quit' to end the program."

active = True

while active :
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)   