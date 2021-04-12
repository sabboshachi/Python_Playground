banned_user = ['andrew' , 'carolina', 'david']
user = "andrew"
if user not in banned_user:
    print(user.title() + " , you can post a response if you wish.")
else:
    print("Please try again")