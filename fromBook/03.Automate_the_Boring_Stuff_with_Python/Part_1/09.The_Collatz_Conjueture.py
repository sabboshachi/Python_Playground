print("Inter a Number: ")
value = int(input())

def collatz(number):
    if number % 2 == 0:
        x = number // 2
    elif number %2 == 1:
        x = (3 * number) + 1
    return x

flag = True
while flag == True:
    output = collatz(value)
    print(output)
    if output == 1:
        flag = False
    else:
        value = output