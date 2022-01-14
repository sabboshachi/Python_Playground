def get_formatted_name(first_name, last_name):
    """Return a dill name , neatly formatted"""
    full_name = first_name.title() + " " + last_name.title()
    return full_name

profile = get_formatted_name("susmita" , "dey !")
print(profile)


#### When we call a function that returns value we need to provide a variabke where the return value can be stored. In this
#### case the returned value is stored in the variable profile.

