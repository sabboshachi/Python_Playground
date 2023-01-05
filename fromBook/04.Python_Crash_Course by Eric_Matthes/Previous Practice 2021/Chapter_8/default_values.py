def describe_book(book_name , book_type="Thriller"):
    """Here we set the default value of a parameter"""
    print("\nMy one of the most favourite book is : " + book_name.title() + "!")
    print("It is a kind of " + book_type + " book!")

describe_book(book_name="harry potter")
describe_book(book_name="the da vinci code")


#### When we use the default values any parameter with a default value needs to be listed after all the parameter that
#### do not have the default values. This allows the python to continue interpreting positional arguments correctly.