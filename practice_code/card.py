''' 
#suit

#rank

'''

from rank import rank
from suit import suit

class card():
    def __init__(self, p_suit, p_rank):
        r = rank()
        valid_rank = r.validate(p_rank)

        s = suit()
        valid_suit = s.validate(p_suit)

        if(valid_rank and valid_suit):
            self.suit = p_suit
            self.rank = p_rank
        else:
            self.suit = "Invalid"
            self.rank = "Invalid"
    def display(self):
        print(self.rank + " of " + self.suit)        

card1 = card("Hearts", "11")
card1.display()
card2 = card("Spades", "2")
card2.display()
card3 = card("Clubs", "King")
card3.display()
card4 = card("Diamonds", "Ace")
card4.display()
card5 = card("Help", "2")
card5.display()
card6 = card("Diamonds", "-2")
card6.display()
card7 = card("Clubs", "kings")
card7.display()