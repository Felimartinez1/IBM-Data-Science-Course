def binary(decimal):
    binary = ''
    while decimal // 2 != 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return str(decimal) + binary
number = int(input('enter the number that you want to convert to binary: '))
print (binary(number))
