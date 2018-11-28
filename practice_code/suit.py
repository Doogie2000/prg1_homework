class suit():
    def __init__(self):
        self.values = {
            "Hearts":0,
            "Diamonds":1,
            "Spades":2,
            "Clubs":3,
            "Invalid":-1
        }

    def validate(self, suit_value) :
        if suit_value in self.values :
            return True
        else :
            return False   