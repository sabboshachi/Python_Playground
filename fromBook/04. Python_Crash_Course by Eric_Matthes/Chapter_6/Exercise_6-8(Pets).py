pet_1 = {
    "name" : "pussy",
    "type" : "cat",
    "owner" : "susmita"
}
pet_2 = {
    "name" : "max",
    "type" : "dog",
    "owner" : "sabboshachi"
}
pet_3 = {
    "name" : "jerry",
    "type" : "rat",
    "owner" : "tom"
}
users = [pet_1, pet_2, pet_3]
for user in users:
    print("\n" + user["name"].title() + " is a " + user["type"].title() + ".")
    print(user["owner"].title() + " is his/her owner.")