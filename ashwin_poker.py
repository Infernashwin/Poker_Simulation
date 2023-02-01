'''
Program Name: ashwin_poker.py (The main program for the OO Poker assignment)
Programmer Name: Ashwin Mayurathan
Date: 4-12-2022
Description: This code is the main code for the OO Poker assignment. It allows the user to play a simple game of poker.

Imports from the Standard_Poker code to have access to the neccessary classes.
'''
from standard_poker import *

def main():
    #Initializes variables.
    game = True
    player_names = []

    #Ask user if they would lke to start the game.
    game = (input("Would you like to start the game? [Y/N]: ") == "Y")

    #If user agrees to a game ask for names of the players.
    if game:
        print("\n")
        print("******************************************************************************************")
        #Ask names for both of the players.
        for i in range(2):
            player_names.append(input(f"Enter Player {i+1}'s Name: "))

    #While a game is in session
    while game:
        print("******************************************************************************************")
        #Start a poker game, deal and evaluate hands.
        poker = Game(player_names)
        poker.deal()
        poker.evaluate()
        print("******************************************************************************************")

        #Ask the user if they would like to play again.
        game = input("Would you like to play again? [Y/N]:") == "Y"

    #Let the user know the code is over.
    print("\n")
    print("Game Over. See You Next Time!")

main()


