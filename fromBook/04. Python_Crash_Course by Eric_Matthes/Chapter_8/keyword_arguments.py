
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + "!")
    print("It's name is " + pet_name.title() + "!" )

describe_pet(animal_type="cat", pet_name="Pussy")

describe_pet(pet_name="max", animal_type="dog")

#### A keyword argument is a name value pair that we pass to a function! We directly assoiate the name and the value
#### within the argument, so when we pass the argument to the function , there is no confusion. And also there is no need
### to worry about the order of arguments!