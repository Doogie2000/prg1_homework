from deck import deck
from card import card

class player ():
    def __init__(self):
        self.score = 0
        self.hand = deck()
    def draw_card (self, draw_pile):
        card = draw_pile.draw()
        self.hand.add_card(card)
    def show_hand (self):
        self.hand.fan()

    def ask_card (self, opponentDeck, draw_pile, card):
        cardFound = False
        for opponent_card in opponentDeck.cards :
            if (opponent_card.rank == card.rank):
                self.hand.add_card(opponent_card)
                opponentDeck.deck.remove(opponent_card)
                cardFound = True
        if cardFound == False :
            self.draw_card(draw_pile)
    def increase_score (self, discardDeck):
        pass
    