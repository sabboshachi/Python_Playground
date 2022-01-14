def build_person(first_name, last_name, age = ""):
    """Return a dictionary of information about a person """
    if age:
        person = {"first": first_name, "last": last_name, "age": age}
    else:
        person = {"first": first_name, "last": last_name}

    return person

profile = build_person("sismita" , "dey") ## With out age
print(profile)

profile = build_person("sismita" , "dey", 23) ## With age
print(profile)

profile = build_person("sismita" , 23 ,"dey",) ## Corrent but wrong order
print(profile)


profile = build_person(first_name="sismita" , last_name="dey",age=23) ## Age int value no problem
print(profile)


profile = build_person(first_name="sismita" , last_name="dey",age="23") ## Age string no problem
print(profile)