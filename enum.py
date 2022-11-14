from enum import Enum
from dataclass import dataclass
FIXED_VACATION_DAYS_PAYOUT = 5 # The fixed nr of vacation days that can be paid out.

@dataclass
class Employee:
    """Basic representation of an employee at the compnay."""
    
    name: str
    role: str
    vacation_days: int = 25
    
    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holiday."""
        if payout:
            # check that there are enough vacation days left for a payout
            raise ValueError(
                f" You don't have enough holidays left over for a payout.\
                    Remaining holidays: {self.vacation_days}"
            )
        try:
            self. 
    

