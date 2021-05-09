def front_back(str):
    length = len(str)
    swap = str[0]
    str[0] = str[length - 1]
    str[length - 1] = swap
    return str

front_back('code')
front_back('a')
front_back('ab')