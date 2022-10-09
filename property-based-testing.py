from functools import reduce
from typing import List

def to_ascii_codes(int: str) -> List[int]:
    return [ord(c) for c in inp]

def from_ascii_codes(inp: List[int]) -> str:
    return reduce(lambda x, y: x + chr(y), inp, "")