def get_formatted_name(first_name, middle_name , last_name):
    """Return a fullname neatky formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

profile = get_formatted_name(first_name="susmita", middle_name="dey", last_name="tip!")
print(profile)


profile = get_formatted_name("susmita", "dey!")  ##  here is one agrument is missing and so the error occurs
print(profile)


### Here we added an if statement but the program is still error.
### Think again and for solution see the third part