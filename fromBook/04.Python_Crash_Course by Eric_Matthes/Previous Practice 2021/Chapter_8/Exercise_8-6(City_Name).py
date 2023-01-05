
def city_country(city, country):
    palace = city + ", " + country
    return palace
while True:
    city_1 = input("\nEnter the name of City: ")
    country_1 = input("Enter the name of country: ")

    palace_1 = city_country(city_1,country_1)
    print(palace_1)

