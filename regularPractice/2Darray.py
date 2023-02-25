# Define a 2D array
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Loop through each row in the array
for row in arr:
    # Loop through each element in the row and print it
    for element in row:
        print(element, end=" ")  # end=" " ensures that elements are printed on the same line
    print()  # print a new line after each row is printed
