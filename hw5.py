#dice roll game
import time
print('''Greetings Professor Falken

Shall we play a game?
''')


while True: 
    y_n = input('''1) Chess
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

name_1 = input ("Player 1: enter name > ")
name_2 = input ("Player 2: enter name > ")

players = {name_1 , name_2 ,}
print (players)
