import random
import time

class dice():
    def __init__(self):
        self.values = [1,2,3,4,5,6]
        side_up = 6

    def player_roll(self) :
        print('''

        Rolling...

        '''
        )
        time.sleep(1)
        print('''
        Your roll is...
        ''')
        side_up = random.randint(1,6)
        print(side_up)
        return side_up
