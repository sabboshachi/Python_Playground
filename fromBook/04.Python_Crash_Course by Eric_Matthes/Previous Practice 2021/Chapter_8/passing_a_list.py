def greet_user(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)

username = ["sandy","Rudra","gulum"]
greet_user(username)