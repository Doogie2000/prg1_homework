from deck import deck
from player import player 

draw_pile = deck(True)
discard_pile = deck()

draw_pile.fan()
discard_pile.fan()

player_count = int(input("How many people are playing? > "))
players = {}
for all_player in range(player_count) :
    players[input("Enter Name > ")] = player()
for a_player in players.values():
    #take turn
    #ask which player you want to question
    #ask if they have your cards
    for _ in range(7):
        player.draw_card(a_player, draw_pile)
for current_player in players.values():
    #take turn
    #ask which player you want to question
    #ask if they have your cards
    print("Players")
    for all_players in players:
        print(all_players)
    ps = 0
    while ps == False:
        player_selection = input("What player do you want to ask? ")
        if player_selection == current_player :
            ps = False
            print("You cannot select yourself. ")
        else: ps = True
    player.show_hand(current_player)
    rank_selection = input("What card do you want to ask for? ")
    for player_card in current_player.hand.cards :
        if rank_selection != player_card.rank :
            Exception("You do not have this card in your hand. ")
    player.ask_card(player_selection, draw_pile, rank_selection)
