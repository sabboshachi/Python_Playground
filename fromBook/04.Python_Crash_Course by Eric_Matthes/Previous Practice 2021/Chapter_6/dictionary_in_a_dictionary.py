uesrs = {
    "susmita" : {
        "first" : "susmita",
        "middle" : "dey",
        "last" : "tip",
        "city" : "dhaka"
    },
    "sobbo" : {
        "first": "sabboshachi",
        "middle": "sarkar",
        "last": "ankan",
        "city": "rajshahi"
    }
}

for username, user_info in uesrs.items():
    print("\nUsername: " + username)
    fullname = user_info["first"] + " " + user_info["middle"] + " " + user_info["last"]
    home = user_info["city"]

    print("\tFullname : " + fullname.title() + ".")
    print("\tLocation : " + home.title() + ".")