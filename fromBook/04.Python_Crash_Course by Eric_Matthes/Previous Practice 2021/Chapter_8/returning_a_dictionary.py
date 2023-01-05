def build_person(first_name, last_name):
    """Return a dictionary of information about a person """
    person = {"first": first_name, "last": last_name}
    return person

profile = build_person("sismita" , "dey")
print(profile)