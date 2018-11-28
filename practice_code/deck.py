from card import card


class deck():
    def __init__(self, cards = []):
        self.cards = cards

    def draw(self):
        draw_card = self.cards[0]
        self.cards.remove(draw_card)
        return draw_card

    def shuffle(self):
        pass
    
    def restock(self, new_cards):
        for c in cards:
            if (c.suit != "invalid" and c.rank != "invalid"):
                self.cards.append(c)
    
    def cut(self):
        #cut randomly
        import random
        
        return deck1, deck2
    
    def split (self):
        #split in half
        return deck1, deck2
    
    def fan(self):
        pass