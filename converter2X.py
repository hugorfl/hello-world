""" Development Exercises – L1

Create a command line program that take as input parameter a number and then
it displays in the console the corresponding number (positive integers Plus
Zero) in Binary and Hexadecimal. It also manages errors using exceptions for
not using numbers. Convert the number using the algorithm and not a function.

:authors: - Hugo Rodríguez
"""

from typing import Any
from utils import require
import sys


def __tuple_to_string(binary_tuple: tuple) -> str:
    return ''.join(map(str, binary_tuple))


def __map_number_to_letter(digit: int) -> int:
    return digit if digit < 10 else chr(ord('A') + digit - 10)


def __convert_int_to_base(number: int, base: int) -> str:
    require(
        number >= 0,
        f'Only positive integers and zero are allowed, "{number}" given'
    )

    if number == 0:
        return "0"

    digits = []
    dividend = number

    while dividend > 0:
        digits.append(__map_number_to_letter(dividend % base))
        dividend //= base

    digits.reverse()
    return __tuple_to_string(tuple(digits))


def __parse_arg_num(number: Any) -> int:
    require(
        isinstance(number, int)
        or (isinstance(number, str) and number.lstrip("-+").isdigit()),
        f'Argument "{number}" is not a valid number'
    )

    return number if not isinstance(number, str) else int(number)


def convert_to_bin(number: Any) -> str:
    return __convert_int_to_base(__parse_arg_num(number), 2)


def convert_to_hex(number: Any) -> str:
    return __convert_int_to_base(__parse_arg_num(number), 16)


def __check_console_input(str_numbers: list):
    require(len(str_numbers) > 1, "No arguments provided")


if __name__ == "__main__":
    try:
        __check_console_input(sys.argv)
        number = sys.argv[1]
        print(f"Number to convert: {number}")
        print("Binary: " + convert_to_bin(number))
        print("Hexadecimal: " + convert_to_hex(number))
    except ValueError as e:
        print(e)
