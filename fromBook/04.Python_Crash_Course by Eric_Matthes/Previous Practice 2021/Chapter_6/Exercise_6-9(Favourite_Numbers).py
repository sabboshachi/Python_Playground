favourite_numbers = {
    "susmita" : [2, 6 , 9],
    "sandy" : [55, 25],
    "sabboshachi" : [23]
}
for k , v in favourite_numbers.items():
    print(k.title() + "'s favourite number is :")
    for number in v:
        print(number)
