class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""

        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is sitting.")

    def walk(self):
        """Simulate a dog walking in response to a command."""
        print(self.name.title() + " is walking.")

my_dog = Dog("Tom", 5)

print("Name of my dog is " + my_dog.name.title() + ".")
print("He's " + str(my_dog.age) + " years old.")

my_dog.walk()
my_dog.sit()
