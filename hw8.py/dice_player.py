from dice import dice

class player():
    def __init__(self):
        player_name = input('''
        What is your player name? 
        >>> ''')            
        turn_wins = 0
        game_wins = 0
    def display_status(self, turn_wins, game_wins, player_name) :
        print(''' 
        ''', player_name,''' 
        ''', turn_wins,''' 
        ''', game_wins)
    def take_turns(self, dice_count) :
        score = 0
        for dice in range(0, dice_count):
            score += dice.player_roll()
        print (score)
        return score
