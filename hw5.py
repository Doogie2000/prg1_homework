#dice roll game
import time
print('''

Greetings Professor Falken

Shall we play a game?
''')


while True: 
    y_n = input('''
    1) Chess
    2) Dice Roll
    3) Checkers
    4) Global Thermonuclear War

    >>>''')
    if (y_n != "2") :
        print("How about a nice game of dice?")
        time.sleep(3)
    elif (y_n == "2") :
        print ("A good choice")
        time.sleep(1)
        break
players={}
player_1 = {}
player_2 = {}
player_1["name"] = input ("player 1: enter name > ")

player_2["name"] = input ("player 2: enter name > ")
players["player_1"] = player_1
players["player_2"] = player_2
print(players)


import random

print('''
#Round''' , round '''
''')
for player in players :
    for ("score") in players[player].values() :

        input(each_value + ": Press enter to roll ")
        time.sleep(2)
        
        player["score"] = random.randint(1,6)
        print(each_value, player["score"])
    wins_1 = 0
    wins_2 = 0
    if players['player_1'] > players['player_2'] :
        print("player_1" + " wins this round")
        wins_1 += 1
    if players["player_2"] > players["player_1"] :
        print("player_2" + " wins")
        wins_2 += 1
    round += 1

