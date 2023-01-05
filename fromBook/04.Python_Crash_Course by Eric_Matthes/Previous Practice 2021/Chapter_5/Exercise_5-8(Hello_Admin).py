usernames = ["sandy","rudra","hulk","admin","thor"]

for username in usernames:
    if username == "admin":
        print("\nHello, " + username.title() + ", would you like to see a status report ?")
    else:
        print("\nHello, " + username.title() + ", thank you for logging in again.")

