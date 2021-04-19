""" Development Exercises – L1
Create a program that parses a file given as parameter and counts the number
of occurrences for a list of words identified in the file. The identification
is sensitive case. The program will accept the words to test as arguments.
English or Spanish.
"""

from itertools import islice
import sys
import re

"""
Test cases:

1 - [TTP] Insert existing filename and one or more keywords
2 - [TTF] Insert non-existing filename and one or more keywords
3 - [TTF] No keywords provided
"""


def checkArgument(expression: bool, errorMsg: str):
    if not expression:
        raise ValueError(errorMsg)


def isArgumentFilename(filename: str) -> bool:
    return re.match(r'^[\w-]+(.[a-zA-Z0-9]+)*$', filename)


def isKeywordValid(keyword: str) -> bool:
    return keyword.isascii()


def checkInput(argsList: list[str]):
    checkArgument(len(argsList) >= 1, 'No filename was given')
    checkArgument(len(argsList) >= 2, 'No keywords were given')
    checkArgument(
        isArgumentFilename(argsList[0]),
        'Filename has invalid characters'
    )

    for keyword in islice(argsList, 1, None):
        checkArgument(
            isKeywordValid(keyword),
            f'Keyword "{keyword}" has wrong format'
        )


def extractKeywords(argsList: list[str]) -> dict[str, int]:
    keywordDict = {}

    for keyword in argsList:
        keywordDict[keyword] = 0

    return keywordDict


def readFileContents(filename: str) -> list:
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        raise ValueError(f'File "{filename}" does not exist')

    contents = file.read()\
        .replace('\n', ' ')\
        .replace('\t', ' ')
    file.close()

    return contents.split(' ')


def parseFile(filename: str, keywords: dict[str, int]):
    contents = readFileContents(filename)
    kwords = keywords.keys()

    for word in contents:
        if word in kwords:
            keywords[word] += 1


def printKeywordOcurrences(keywords: dict[str, int]):
    kwords = keywords.keys()

    for kword in kwords:
        print(kword + ': ' + str(keywords[kword]) + ' ocurrences')


try:
    checkInput(sys.argv[1:])
    keywordsDict = extractKeywords(sys.argv[2:])
    parseFile(sys.argv[1], keywordsDict)
    printKeywordOcurrences(keywordsDict)
except ValueError as e:
    print(e)
