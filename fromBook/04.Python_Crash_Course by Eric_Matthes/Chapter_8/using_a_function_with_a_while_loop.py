def build_person(first_name, last_name):
    """Return a dictionary of information about a person """
    full_name = first_name + " " + last_name
    return full_name

## this is an infinite loop

while True:
    print("\nPlease Tell me your name :")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")

    formatted_name = build_person(f_name, l_name)
    print("\nHello," + formatted_name + "!")
