# Function to check if a number is palindrome
def is_palindrome(num):
    # Convert the number to a string and reverse it
    reversed_num = str(num)[::-1]
    # Check if the original and reversed number are equal
    if str(num) == reversed_num:
        return True
    else:
        return False

# Example usage
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
