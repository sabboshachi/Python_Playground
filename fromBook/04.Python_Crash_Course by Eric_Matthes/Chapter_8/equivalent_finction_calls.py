def describe_book(book_name , book_writter, book_type="Thriller"): ### this one is corrent and it will run with any error
    """Here we set the default value of a parameter"""
    print("\nMy one of the most favourite book is : " + book_name.title() + "!")
    print("It is a kind of " + book_type + " book!")
    print("The writter of the book is " + book_writter.title() + "!")

describe_book("harry potter" , "j k rowling")
describe_book(book_name="harry potter" , book_writter="j k rowling")
describe_book(book_writter="j k rowling", book_name="harry potter" )
describe_book(book_name="harry potter" , book_writter="j k rowling", book_type="Horror")

### So this means we can change the default value when ever we want in a function calling

#describe_book(book_name="the da vinci code", book_writter="dan brown")