def cars_info(manufacturer,model,**features):
    car = {}
    car["Company"] = manufacturer
    car["Model"] = model
    for k , v in features.items():
        car[k] = v
        return car

car_details = cars_info("Buggati", "Veron", color= "black", speed= "400km/hr") ### last value isn't printing ###
print(car_details)