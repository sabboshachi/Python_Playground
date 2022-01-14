#start with user that need to be verified
#and an empty list to hold confirmed users

unconfirmed_users =  ["sandy" , "rudra" , "gulum"]
confirmed_users = []

#verify each user untill there are no more unconfirmed users
#move each verified users into the list of confirmed users

while unconfirmed_users:
    currnet_users = unconfirmed_users.pop()

    print("verified users :" + currnet_users.title())
    confirmed_users.append(currnet_users)

    ## display all confirmed users

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())