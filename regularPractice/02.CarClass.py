class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descritive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car("BMW", "a4", 2016)

print(my_new_car.get_descriptive_name())

