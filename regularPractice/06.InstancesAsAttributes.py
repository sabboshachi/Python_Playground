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

class Battery():
    """A simple attempt ot model a battery for an electric car."""

    def __init__(self, batttery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = batttery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 280

        print("This car can go approximately " + str(range) + " miles on full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, model, make, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have a gas tank."""
        print("This car doesn't need a gas tank.")


my_tesla = ElectricCar("Tesla", "Model S", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


### From this code we can import any saved classes for our future code