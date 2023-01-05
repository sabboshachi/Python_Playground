cities = ["dhaka" , "dehle", "london", "rajshahi"]

bd_cities = {
    "dhaka" : {
        "country" : "bangladesh",
        "population" : "20 Million",
        "fact" : "dirty"
    },
    "dehle" : {
        "country" : "india",
        "population" : "10 Million",
        "fact" : " very dirty"
    },
    "london": {
        "country": "uk",
        "population": "7 Million",
        "fact": "clean"
    },

}
for k, v in bd_cities.items():
    if k in cities:
        print("\n" + k.title() + " is a city of " + v["country"].title() + ".")
        print(k.title() + " is has a population of " + v["population"].title() + ".")
        print("The most interesting fact about " + k.title() + " is, it is " + v["fact"].title() + ".")
    elif k not in  cities:
        print("\n" + k.title() + " is not registered!")



   #if city in bd_cities.keys():
       # print("Registered City.")
        #for k , v in bd_cities.items():

        #print(k.title() + " is a city of " + v["country"] + ".")
       # print(k.title() + " is has a population of " + v["population"] + ".")
        #print("The most interesting fact about " + k.title() + " is, it is " + v["fact"] + ".")


