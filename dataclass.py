import string
from dataclasses import dataclass, field

@dataclass

class Vehicle:
    brand: str
    catalogue_price: int
    electric: bool
    license_plate: str = field(init=False)
    
    def __post_init__(self):
        self.license_plate = generate_vehicle_license()
        
    @property
    def tax(self) -> int:
        tax_rate = 0.02 if self.electric else 0.05
        return int(tax_rate * self.catalogue_price)
    
def main():
    tesla = Vehicle("Tesla Model 3", 600000, True)
    volkswagen = Vehicle("Volkswagen", 350000, True)
    print(tesla.tax)
    print(volkswagen.tax)
    
    
if __name__ == "__main__":
    main()
        