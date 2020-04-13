"""

This is a python game.  There will be a player and Monster
The attributes of the player will be name, attack, heal, health
The attributes of the Monsters will be name, attack, health
If Monster health is less than zero, player wins


"""
import os

player_name = input("What is your name? ")
mons_name = input("What is the monster's name? ")
print("")
game_running = False

os.system('cls')

while game_running is True:
    player = {'name': player_name, 'attack': 10, 'heal': 16, 'health': 100}
    mons = {'name': mons_name, 'attack': 12, 'health': 100}

    new_round = True
    while new_round is True:
        player_won = False
        mons_won = False

        print('Select your action')
        print('1) Attack')
        print('2) Heal')
        print('3) Quit')

        player_action = input()
        os.system('cls')

        if player_action == '1':
            mons['health'] = mons['health'] - player['attack']
            player['health'] = player['health'] - mons['attack']
            print(player_name + " strikes the monster with a mighty blow")
            print(mons_name + "'s" + " health is now " + str(mons['health']))
            if mons['health'] <= 0:
                player_won = True
            print("")
            print(mons_name + " strikes back with a mighty blow")
            print(player_name + "'s" + " health is now " + str(player['health']))
            if player['health'] <= 0:
                mons_won = True
            print("")
        elif player_action == '2':
            print(player_name + "makes the smart move and applies a heal")
            print("")
            player['health'] = player['health'] + player['heal']
        elif player_action == '3':
            new_round = False
            game_running = False
        else:
            print('Wrong choice, try again!')

        if mons_won is True:
            print(player_name + " is now dead!!")
            quit = input("Do you want to continue? ")
            if quit == "n":
                new_round = False
                game_running = False
            else:
                player_won == True
            print(player_name + " has defeated the evil monster " + mons_name)
            new_round = False
            game_running = False
