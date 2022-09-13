import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

class Person:
    def __init__(self, name: str, adress: str):
        self.name = name
        self.adress = adress
        
    def __str__(self) -> str:
        return f"{self.name}, {self.adress}"
        
def main() -> None:
    person = Person(name="John", adress="123 Main St")
    print(person)
        
if __name__ == "__main__":
    main()