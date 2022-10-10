from functools import reduce
from typing import List

def to_ascii_codes(int: str) -> List[int]:
    return [ord(c) for c in inp]

def from_ascii_codes(inp: List[int]) -> str:
    return reduce(lambda x, y: x + chr(y), inp, "")


# initializing list
lis = [1, 3, 5, 6, 2]
 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
#print("The maximum element of the list is : ", end="")
#print(functools.reduce(lambda a, b: a if a > b else b, lis))


"""Unit Test: Arrange, Act, Assert
Produces own data to test the code
Related to "What is the code doing"

Property test: relay on example data

Functions: The ord() function returns an integer representing the Unicode character.

            Lambda function: A lambda function can take any number of arguments, but can only have one expression.
            x = lambda a : a + 10, -> x(5) = 15
            x = lambda a, b c: a + b + c, x(5, 6, 2) = 13
            
            char(): The chr() function returns the character that represents the specified unicode.
            x = char(97), -> a
"""