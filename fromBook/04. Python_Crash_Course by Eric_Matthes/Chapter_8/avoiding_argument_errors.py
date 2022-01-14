def describe_book(book_name , book_writter, book_type="Thriller"):
    """Here we set the default value of a parameter"""
    print("\nMy one of the most favourite book is : " + book_name.title() + "!")
    print("It is a kind of " + book_type + " book!")
    print("The writter of the book is " + book_writter.title() + "!")


describe_book() ## Here the error occurs because we did not give any arguments to pass the function ##
describe_book(book_name="the da vinci code", book_writter="dan brown") ## This one will run without any problem ##