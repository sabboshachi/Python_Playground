prompt = "\nTell me something, and I will repaet it back to you: "
prompt += "\nEnter 'Quit' to end the program."

message = ""

while message != "quit":
    message = input(prompt)
    print(message)
