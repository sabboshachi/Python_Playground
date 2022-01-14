def build_person(first_name, last_name, middle_name = ""):
    """Return a dictionary of information about a person """
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name

    else:
        full_name = first_name + " " + last_name

    return full_name.title()

while True:
    print("\nPlease Tell me your name :")

    f_name = input("First Name: ")
    l_name = input("Last Name: ")

    m_name = input("Middle Name: ")

    formatted_name = build_person(first_name=f_name, middle_name=m_name, last_name=l_name)
    print("\nHello, " + formatted_name + "!")

    condition = input("\nDo you want to continue? (Yes/No) :")
    if condition == "no":
        break



