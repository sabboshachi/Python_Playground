# Initialize the product variable
product = 1

# Initialize the counter variable
counter = 1

# Use a while loop to iterate 10 times
while counter <= 10:
    # Get the number from the user
    number = int(input("Enter number {}: ".format(counter)))
    # Multiply the product by the number
    product *= number
    # Increment the counter
    counter += 1

# Print the final product
print("The product of the numbers is:", product)
