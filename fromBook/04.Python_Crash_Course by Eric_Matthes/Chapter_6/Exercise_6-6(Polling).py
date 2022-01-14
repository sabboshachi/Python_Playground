fav_languages = {
    "susmita" : "python",
    "sandy" : "c",
    "rudra" : "ruby",
    "sobbo" : "python"
}

peoples = ["panda" , "sarkar" , "niaj" , "legend", "sandy", "susmita"]
for name in peoples:
    if name in fav_languages.keys():
        print("Hello! " + name.title())
    else:
        print(name.title() + " are not an user, please sign up. ")


