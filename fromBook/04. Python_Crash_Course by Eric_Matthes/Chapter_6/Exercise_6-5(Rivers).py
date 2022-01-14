rivers = {
    "padma" : "bangladesh",
    "ganga" : " india",
    "nile" : " egypt"

}
for k , v in rivers.items():
    print("The " + k.title() + " runs through " + v.title() + "!")

#printing the name of rivers using loop

for river in rivers.values():
    print(river.title())
#printing the name of countries using loop
for country in rivers.keys():
    print(country.title())