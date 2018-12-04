''' 
#suit

#rank

'''

from rank import rank
from suit import suit

class card():
    def __init__(self, p_suit, p_rank):
        ranks = rank()
        valid_rank = ranks.validate(p_rank)

        suits = suit()
        valid_suit = suits.validate(p_suit)

        if(valid_rank and valid_suit):
            self.suit = p_suit
            self.rank = p_rank
        else:
            raise ValueError("Invalid Rank or Suit")

    def display(self):
        print(self.rank + " of " + self.suit)        