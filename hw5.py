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
players['player_1'] = input ("player 1: enter name > ")

players['player_2'] = input ("player 2: enter name > ")

print(players)
'''
import random

print('''
#Round 1
''')

for player in players :

    input(players[player] + ": Press enter to roll ")
    time.sleep(2)

    dice_roll = random.randint(1,6)
    
    players['score'] = int(dice_roll)
    print(players[player], player['score'])
wins_1 = 0
wins_2 = 0
if players['player_1'] > players['player_2'] :
    print("player_1" + " wins this round")
    wins_1 += 1
if players["player_2"] > players["player_1"] :
    print("player_2" + " wins")
    wins_2 += 1

print('''
#Round 2
''')
for player in players :

    input(player + ": Press enter to roll ")
    time.sleep(2)

    dice_roll = random.randint(1,6)
    
    players[player] = dice_roll
    print(player, players[player])

if players["player_1"] > players["player_2"] :
    print("player_1" + " wins this round")
    wins_1 += 1
elif players["player_2"] > players["player_1"] :
    print("player_2" + " wins this round")
    wins_2 += 1


if wins_1 >= 2 :
    print("player_1" +  " wins!")
elif wins_2 >= 2 :
    print ("player_2" + " wins!")

print('''
#Round 3
''')
for player in players :

    input(player + ": Press enter to roll ")
    time.sleep(2)

    dice_roll = random.randint(1,6)
    
    players[player] = dice_roll
    print(player, players[player])

if players["player_1"] > players["player_2"] :
    print("player_1" + " wins this round")
    wins_1 += 1
elif players["player_2"] > players["player_1"] :
    print("player_2" + " wins this round")
    wins_2 += 1

if wins_1 >= 2 :
    print("player_1" + " wins!")
elif wins_2 >= 2 :
    print ("player_2" +" wins!")
'''