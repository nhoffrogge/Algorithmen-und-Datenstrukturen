#from ctypes import addressof
import string
import random
from dataclasses import dataclass, field
from typing import List

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k= 12))



@dataclass(frozen=False)
class Person:
    name: str
    adress: str
    #vinf: list[str] = field(default_factory = str)
    email_adresses: List[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.adress}"


def main() -> None:
    person = Person(name = "John", adress = "123 Main St")
    person.name = "Nils" 
    print(person)       

if __name__ == "__main__":
    main()