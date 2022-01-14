
numbers = list(range(101))
print(numbers)

cubed_value = []

for number in numbers:
    cube = number ** 3
    print(cube)

    cubed_value.append(cube)

print(cubed_value)
