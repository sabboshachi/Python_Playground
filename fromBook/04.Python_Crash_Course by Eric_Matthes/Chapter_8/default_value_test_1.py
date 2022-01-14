def describe_book(book_name , book_type="Thriller", book_writter): ## here the program will not run as there is  there is an error of caused by the order of the default value
    """Here we set the default value of a parameter"""
    print("\nMy one of the most favourite book is : " + book_name.title() + "!")
    print("It is a kind of " + book_type + " book!")
    print("The writter of the book is " + book_writter.title() + "!")


describe_book(book_name="harry potter" , book_writter="j. k. rowling")
describe_book(book_name="the da vinci code", book_writter="dan brown")


def describe_book(book_name , book_writter, book_type="Thriller"): ### this one is corrent and it will run with any error
    """Here we set the default value of a parameter"""
    print("\nMy one of the most favourite book is : " + book_name.title() + "!")
    print("It is a kind of " + book_type + " book!")
    print("The writter of the book is " + book_writter.title() + "!")


describe_book(book_name="harry potter" , book_writter="j k rowling")
describe_book(book_name="the da vinci code", book_writter="dan brown")