class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 150

    def get_descriptive_name(self):
        """Return a neatly formatted descritive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # """Set the odometer reading to the given value."""
        # self.odometer_reading = mileage

        """Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car("BMW", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(200)
my_new_car.read_odometer()


