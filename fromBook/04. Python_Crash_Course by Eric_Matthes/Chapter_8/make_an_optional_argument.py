def get_formatted_name(first_name, middle_name , last_name):
    """Return a fullname neatky formatted"""

    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

profile = get_formatted_name(first_name="susmita", middle_name="dey", last_name="tip!")
print(profile)


profile = get_formatted_name(first_name="susmita", last_name="tip!")  ##  here is one agrument is missing and so the error occurs
print(profile)