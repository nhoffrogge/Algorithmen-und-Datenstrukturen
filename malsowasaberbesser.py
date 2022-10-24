import string
import random
from dataclasses import dataclass

def generate_id() -> str:
    return "".join(random.choise(string.ascii.uppercase, k=12))
    
@dataclass
class Person:
    name: str
    adress: str
    
def main() -> None:
    person = Person(name="John", adress="123 Main St")
    print(person)
    
if __name__() == "__main__":
    main()