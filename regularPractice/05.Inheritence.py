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
    def increment_odometer(self, miles):
        """Add the fiven amount to the odometer reading."""
        self.odometer_reading += miles


# my_new_car = Car("BMW", "a4", 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.increment_odometer(135)
# my_new_car.read_odometer()

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, model, make, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have a gas tank."""
        print("This car doesn't need a gas tank.")
        



my_tesla = ElectricCar("Tesla", "Model-S", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

