from dice import dice
from dice_player import dice_player

class dice_roll_game():
    def __init__(self):
        player_count = int(input("How many players will be playing? "))
        all_players = {}
        for player in range(player_count):
            all_players[input("Enter Name > ")] = player()
    def play(self):
        dice_count = int(input("how many dice for this game? "))
        for player in all_players :
            print(take_turns(dice_count))
            
    
