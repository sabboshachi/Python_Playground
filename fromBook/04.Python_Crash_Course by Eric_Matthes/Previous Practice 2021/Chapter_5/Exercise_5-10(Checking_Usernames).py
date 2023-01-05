current_users = ["sandy", "rudra", "susmita", "tip", "sabboshachi"]
print(current_users)

new_users = ["akib", "nur", "pallab", "udoy", "sabboshachi"]
print(new_users)

for new_user in new_users:

    if new_user in current_users:
        print("Sorry. " + new_user.title() + "! \n\tThis name isn't avaiable. ")
    else:
        print(new_user.title() + "! \n\tThis name is avaiable.")
