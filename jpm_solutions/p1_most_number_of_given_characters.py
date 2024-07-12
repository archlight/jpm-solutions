"""
Problem 1:

Given a long statement and a input letter, find the word which contains the most number of the given character. 
If more than one word has the exact same number of the given letter, 
it should return the word with the most number of total letters, 
if more than one words have equal number of given character and total number of characters 
return the word that appeared first in the given statement.
"""


def solution(statement: str, input_char: str):
    if len(input_char) > 1:
        raise Exception("Input invalid: only character supported")
    tokens = statement.split(" ")
    max_count = 0
    result = ""
    for token in tokens:
        c = list(token).count(input_char)
        if c > max_count:
            result = token
            max_count = c
        elif c == max_count and len(result) and len(token) > len(result):
            result = token
    return result
