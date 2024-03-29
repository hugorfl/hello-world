""" Development Exercises – L1
Create a program that parses a file given as parameter and counts the number
of occurrences for a list of words identified in the file. The identification
is sensitive case. The program will accept the words to test as arguments.
English or Spanish.
"""

import re
import sys
from typing import List, Tuple, Dict
from utils import require


def __is_argument_a_filename(filename: str):
    require(filename.strip(), "Filename cannot be empty")
    require(
        re.match(r'^[\w-]+(\.[a-zA-Z0-9]+)*$', filename) is not None,
        'Filename has invalid characters'
    )


def __is_keyword_valid(keyword: str) -> bool:
    return keyword.isascii()


def __require_valid_keywords(key_args: Tuple[str]):
    require(len(key_args), 'No keywords were given')

    for keyword in key_args:
        require(
            __is_keyword_valid(keyword) is not None,
            f'Keyword "{keyword}" has wrong format'
        )


def __map_keywords(key_args: Tuple[str]) -> Dict[str, int]:
    keywords = {}

    for keyword in key_args:
        keywords[keyword] = 0

    return keywords


def __f_read_contents(filename: str) -> List[str]:
    contents = []

    try:
        with open(filename, 'r') as file:
            contents = file.read()\
                .replace('\n', ' ')\
                .replace('\t', ' ')\
                .split(' ')
    except FileNotFoundError:
        raise ValueError(f'File "{filename}" does not exist')

    return contents


def f_find_words(filename: str, *key_args: str) -> Dict[str, int]:
    __is_argument_a_filename(filename)
    __require_valid_keywords(key_args)

    contents = __f_read_contents(filename)
    keywords = __map_keywords(key_args)
    kwords = keywords.keys()

    for word in contents:
        if word in kwords:
            keywords[word] += 1

    return keywords


def __check_console_input(args: List[str]):
    require(len(args) >= 1, 'No filename was given')
    require(len(args) >= 2, 'No keywords were given')


def print_keyword_ocurrences(keywords: Dict[str, int]):
    kwords = keywords.keys()

    for kword in kwords:
        print(kword + ': ' + str(keywords[kword]) + ' ocurrences')


if __name__ == "__main__":
    try:
        __check_console_input(sys.argv[1:])
        keywords = f_find_words(sys.argv[1], *sys.argv[2:])
        print_keyword_ocurrences(keywords)
    except ValueError as error:
        print(error)
