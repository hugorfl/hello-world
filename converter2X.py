""" Development Exercises – L1

Create a command line program that take as input parameter a number and then
it displays in the console the corresponding number (positive integers Plus
Zero) in Binary and Hexadecimal. It also manages errors using exceptions for
not using numbers. Convert the number using the algorithm and not a function.

:authors: - Hugo Rodríguez
"""

import sys

"""
Test Cases:

1 - [TTP] Insert positive integer number
2 - [TTP] Insert 0
3 - [TTP] Insert integer number with leading zeros
4 - [TTP] Insert large numbers (Eg. 68719476736)
5 - [TTF] Insert -1
6 - [TTF] Insert floating point number
7 - [TTF] Insert alphanumeric
8 - [TTF] Insert regular characters
9 - [TTF] Insert symbols
10 - [TTF] No arguments provided

TTP: Test to pass
TTF: Test to fail
"""


def tupleToString(binaryTuple):
    return ''.join(map(str, binaryTuple))


def mapNumberToLetter(digit):
    return digit if digit < 10 else chr(ord('A') + digit - 10)


def convertIntToBase(number, base):
    if number <= 0:
        return (0,)

    digits = []
    dividend = number

    while dividend > 0:
        digits.append(mapNumberToLetter(dividend % base))
        dividend = int(dividend / base)

    digits.reverse()
    return tuple(digits)


def convertToBin(number):
    return convertIntToBase(number, 2)


def convertToHex(number):
    return convertIntToBase(number, 16)


def checkArgument(expression, errorMsg):
    if not expression:
        raise ValueError(errorMsg)
    return


def parseInput(strNumbersList, index):
    checkArgument(len(strNumbersList) > 1, "No arguments provided")
    checkArgument(
        strNumbersList[index].lstrip("-+").isdigit(),
        f"Argument \"{strNumbersList[index]}\" is not a valid number")

    number = int(strNumbersList[index])
    checkArgument(
        number >= 0,
        'Only positive integers and zero are allowed, "'
        + strNumbersList[index] + '" given'
    )
    return number


try:
    number = parseInput(sys.argv, 1)
    print(f"Number to convert: {number}")
    print("Binary: " + tupleToString(convertToBin(number)))
    print("Hexadecimal: " + tupleToString(convertToHex(number)))
except ValueError as e:
    print(e)
