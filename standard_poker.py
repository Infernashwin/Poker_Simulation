'''
Program Name: Standard_Poker.py (The program containing classes for the OO Poker assignment)
Programmer Name: Ashwin Mayurathan
Date: 4-12-2022
Description: This code contains the HAND CLASS and the GAME CLASS used in the OO Poker assignment.

Imports classes from the standard_deck code.
'''
from standard_deck import *
'''
HAND CLASS: A class to represent the hand given to each player.
'''
class Hand():
    #Declares constants within the class.
    STANDARD_DICT = {"Ace":1, "2":2, "3":3, "4":4, "5":5,
                                  "6":6, "7":7, "8": 8, "9":9, "10":10,
                                  "Jack":11, "Queen":12, "King":13}            

    HAND_TYPES = ("Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight",
                    "Three of a Kind", "Two Pair", "Pair", "High Card")

    '''
    __init__: Initializes all attributes of the HAND CLASS. Takes in a parameter player to name the owner of the hand.

    player -> A string which contains the name of a player.
    '''
    def __init__(self, player):
        self.name = player #Name of the player.

        self.all_cards = [] #Cards the player has.

        self.card_val = [] #The values of the cards in the hand.

        self.card_suits = set() #The different suits contained in the hand.

        self.hand_evals = [] #The evalutaion of the hand stored in a list.
                             #First index is the name of the hand (ex. High Card, Flush).
                             #Second index is the important cards of the hand.
                             #Example for a pair, the value of the card thats a pair.

    '''
    add_card: Adds a card into the Hand Class. Takes in the card as a parameter and adds
              the card is stored it in self.all_cards.

    card -> A Card object created by the CARD CLASS.
    '''
    def add_card(self, card):
        #Adds a card to the hand.
        self.all_cards.append(card)

    '''
    show_cards: Prints the cards stored within the hand.
    '''
    def show_cards(self):
        #Prints whoever's hand is being printed.
        print(f"{self.name}'s Hand:\n")

        #Loops through the cards currently in the hand, and prints them.
        for order, card in enumerate(self.all_cards, start = 1):
            print(f"Card {order}: {card.get_name()}")

        #Adds a space.
        print("\n")

    '''
    organize_hand: Organizes the hand and finds the information neccesary to name the hand and then assigns
                   a value to self.hand_evals.
    '''    
    def organize_hand(self):
        #Resets the value of the cards assosiated with the hand.
        self.card_val = []

        #For every card in the hand store the value of the card in the list called self.card_val
        #and store each unique suit in the set called self.card_suits.
        for card in self.all_cards:
            self.card_val.append(card.get_value())
            self.card_suits.add(card.get_suit())
        
        #Checks if a user has a particular hand, and stores the important cards associated with said hand.

        flush = [(len(self.card_suits) == 1), self.high_card_search()]  #Checks if the user has a Flush.

        four_of_a_kind = self.kind_check(4,1) #Checks if the user has a Four of a Kind.

        three_of_a_kind = self.kind_check(3,1) #Checks if the user has a Three of Kind.

        two_pairs = self.kind_check(2,2) #Checks if the user has a Two Pair.

        pair = self.kind_check(2,1) #Checks if the user has a Pair.

        #Checks if user has a Straight.
        #Checks if the difference between the values of highest and lowest cards are 4.
        straight = [(max(self.card_val) - min(self.card_val) == 4), self.high_card_search()]
        #Checks if the hand is full of unique cards (No Repeating Cards, No Pairs/Three of Kinds/Four of Kinds).
        straight[0] =  (straight[0] and not(four_of_a_kind[0] + three_of_a_kind[0] + two_pairs[0] + pair[0]))

        #Checks if the user has a Full House (The user has both a Pair and a Three of a Kind).
        full_house = [(three_of_a_kind[0] and pair[0]), [three_of_a_kind[1][0], pair[1][0]]]

        #Checks if user has a Straight Flush (The user has both a Straight and a Flush).
        straight_flush = [(straight[0] and flush[0]), self.high_card_search()]

        #Creates a list which indexes correspond with the HAND_TYPES array (High Card not included).
        hand_evals = [straight_flush ,four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, pair]

        #Finds out what hand the user has, and stores the important cards associated with the hand.
        self.hand_evals = self.set_eval(hand_evals)

    '''
    set_eval: Figures out the name associated with the hand.
    '''
    def set_eval(self, evals):
        #Loops for the types of Hands.
        for index, check in enumerate(evals, start = 0):
            #Checks if the the player has a certain hand.
            if (check[0]):
                #Returns name based on the index number of the hand, and the important card values associated with the hand.
                return(Hand.HAND_TYPES[index], check[1])

        #If no hand was recognized then the hand is a High Card, so retun High Card as name, and the highest card value.
        return ("High Card", self.high_card_search())

    '''
    high_card_search: Finds the highest card stored in the hand.
    '''
    def high_card_search(self):
        #Returns the highest card in the hand's value.
        return [max(self.card_val)]

    '''
    kind_check: Checks if the card is a Four of a Kind/Three of a Kind/Two Pair/Pair. It takes in 2 parameters, kind and num.

    kind -> refers to what hand we are looking for:
            4 -> Four of a Kind.
            3 -> Three of a Kind.
            2 -> Two Pair/Pair.
    
    num -> refers to the number of Four of a Kind/Three of a Kind/Two Pair/Pair we are looking for (Just differentiates Two Pair and Pair):
            1 -> We are looking for a Four of a Kind/Three of a Kind/Pair.
            2 -> We are looking for a Two Pair.
    '''
    def kind_check(self, kind, num):
        #Initializes variables count and cards.
        count = 0 #The number of times a Four of a Kind/Three of a Kind/Two Pair/Pair is found.
        cards = [] #The value of the  Four of a Kind/Three of a Kind/Two Pair/Pair found.

        #For every value of a card could have.
        for value in Hand.STANDARD_DICT:
            #If there number of times the card appears is the same as the value associated with kind.
            if (self.card_val.count(Hand.STANDARD_DICT[value]) == kind):
                #Store that card value associated with the Four of a Kind/Three of a Kind/Two Pair/Pair found.
                cards.append(Hand.STANDARD_DICT[value])
                #Increases count as a Four of a Kind/Three of a Kind/Two Pair/Pair is found.
                count += 1

        #Reverses the order of cards as they currently are in asscending order.
        #We want decending order as then the highest card values are the first index.
        cards.sort(reverse = True)

        #If there was no card found, then store 0 in card.
        if cards == []:
            cards.append(0)

        #Returns if the right number of Four of a Kind/Three of a Kind/Two Pair/Pair is found and the value of the 
        #Four of a Kind/Three of a Kind/Two Pair/Pair found.
        return (count == num, cards)  


    '''
    get_eval: Returns the name of the hand and the important cards associated with the hand. This data is stored
              in self.hand_evals.
    '''
    def get_eval(self):
        #Returns the evaluation and important cards.
        return self.hand_evals

    '''
    get_player: Returns the name of the player. The name of the player is stored in self.name.
    '''
    def get_player(self):
        #Returns the name of the player.
        return self.name

    '''
    get_hand_types: Returns the constant HAND_TYPES so it can be used outside of the HAND CLASS.
    '''
    def get_hand_types(self):
        #Returns the tuple HAND_TYPES which contains all the different types of hands.
        return Hand.HAND_TYPES

    '''
    get_cards: Returns all the card objects stored in the hand within the attribute self.all_cards.
    '''    
    def get_cards(self):
        #Returns all cards stored in the hand.
        return self.all_cards

    '''
    get_suits: Returns all the suits found within the hand.
    '''    
    def get_suits(self):
        #Returns all cards stored in the hand.
        return self.card_suits

'''
GAME CLASS: A class to represent the actual poker game.
'''
class Game():
    #Declares constants of the GAME CLASS.  
    PLAYER_ONE = "Player One"
    PLAYER_TWO = "Player Two"
    PLAYER_LIST = (PLAYER_ONE, PLAYER_TWO)
    STANDARD_DICT = {"Ace":1, "2":2, "3":3, "4":4, "5":5,
                                  "6":6, "7":7, "8": 8, "9":9, "10":10,
                                  "Jack":11, "Queen":12, "King":13}   
    CARD_NAMES = list(STANDARD_DICT.keys())
    CARD_VALUES = list(STANDARD_DICT.values())

    '''
    __init__: Initializes the attributes of the GAME CLASS. Takes in a parameter player_names to name the players.

    player_names -> A list that contains two strings to name the players.
    '''
    def __init__(self, player_names):
        self.hands = {} #Initalizes dictionary that stores the hands in this game.

        #Populates the dictionary. The Key is simply a string to identify who is player 1 and player 2. 
        #The value stored is simply a Hand object.
        for index, player in enumerate(Game.PLAYER_LIST, start = 0):
            self.hands[player] = Hand(player_names[index])

        self.deck = Deck() #Initializes self.deck to store the deck object.

    '''
    deal: Deals cards from the deck into the hands.
    '''
    def deal(self):
        self.deck.shuffle() #Shuffles the deck.

        #Deals 5 cards to each player.
        for i in range(5):
            #For every player.
            for player in self.hands:
                #Let the user click enter before dealing the next card to slow down the output.
                input("Click Enter to Deal The Next Card")
                #Add a card to the Hand object.
                self.hands[player].add_card(self.deck.get_card())
                #Prints out the hand of the user.
                self.show_hands()
        
        #Allows the user to change cards.
        self.change_cards()

        #Organizes the hand of all players.   
        for player in Game.PLAYER_LIST:
            self.hands[player].organize_hand()

    '''
    show_hands: Prints the hand of each player.
    '''
    def show_hands(self):
        print("******************************************************************************************")
        #For every player, show what cards are in their hand.
        for player in Game.PLAYER_LIST:
            self.hands[player].show_cards()
        print("******************************************************************************************")

    '''
    change_cards: Allows player one to change their cards.
    '''
    def change_cards(self):
        #Shows the hand of player one.
        self.hands[Game.PLAYER_ONE].show_cards()

        #Asks the user which cards they want to switch.
        cards_to_switch = input("Please enter the card number of the card(s) you wish \nto swap " + 
                                "(Leave blank if you wish not to switch cards): ").split()

        #Loops through the cards the user selected.
        for i in range(len(cards_to_switch)):
            #Returns the card to the bottom of the deck.
            self.deck.return_card(self.hands[Game.PLAYER_ONE].get_cards()[int(cards_to_switch[i])-1])
            #Gives user a new card.
            self.hands[Game.PLAYER_ONE].get_cards()[int(cards_to_switch[i])-1] = (self.deck.get_card())

        print("******************************************************************************************")
        print("Final Hands:")
        #Prints the final hands of both players.
        self.show_hands()
        
    '''
    evaluate: Evaluates the two hands and compares them to say which player won, or if the players tied.
    '''
    def evaluate(self):
        #Initializes variables for the evaluate method
        message = 2 #By default print index two of message (It will be defined later in the code).
        messages = [] #A list of possible messages (Will be populated with elements as the code goes on).
        evaluate_dict = {}#A dictionary of each of the player's hand, and the important cards associated with the hand
                          #(Will be populated as the code goes on).
        
        #Loop through all of the players
        for player in self.hands:
            #Populate evaluate_dict with the a key to indentify the player, and the value a list which contains
            #the type of hand, and the import cards associated with the hand.
            evaluate_dict[player] = self.hands[player].get_eval()
            #Creates a message for the player to say they won, and appends that message to the player list
            #(Index 0 will store the victory message for player one, and index 1 does the same but for player two).
            messages.append(f"{self.hands[player].get_player()} Won")

            #Creates a message to print what type of hand the player has (Right now it will only be the type of hand).
            card_message = f"{Game.CARD_NAMES[Game.CARD_VALUES.index(evaluate_dict[player][1][0])]}"

            #If the player has a Full House (which means they have 2 important cards, the Three of a Kind and double),
            #create a specialized message tailored for the Full House hand.
            if (evaluate_dict[player][0] == "Full House"):
                card_message += " over " 
                card_message += f"{Game.CARD_NAMES[Game.CARD_VALUES.index(evaluate_dict[player][1][1])]}"
                #Creates a final message along the lines of "Full House, X over Y".
                #X -> The value of the cards which are a Three of a Kind.
                #Y -> The value of the cards which are a Pair.

            #If the player has a Two Pair (which means they have 2 important cards as there are two pairs),
            #create a specialized message tailored for the Two Pair hand.
            if (evaluate_dict[player][0] == "Two Pair"):
                card_message += " and "
                card_message += f"{Game.CARD_NAMES[Game.CARD_VALUES.index(evaluate_dict[player][1][1])]}"
                #Creates a final message along the lines of "Two Pair, X and Y".
                #X -> The value of the cards apart of the highest pair.
                #Y -> The value of the card apart of the lower pair.

            #If the player has a Flush or Straight Flush (which means the suits are important),
            #create a specialized messaged tailored for Flushes and Straight Flushes.
            if ((evaluate_dict[player][0] == "Flush") or (evaluate_dict[player][0] == "Straight Flush")):
                card_message += " with "
                card_message += "".join(self.hands[player].get_suits()) #.join is a method of sets wich allows
                                                                        #them to be printed as a string.

                #Creates a final message along the lines of "Flush, X with Y".
                #X -> The value of the highest card in the hand.
                #Y -> The common suit among the cards.

            #Prints out the hand the player has.
            print(f"{self.hands[player].get_player()} has a {evaluate_dict[player][0]}, {card_message}")

        #Stores the "Tie Game" as index 2 of messages.
        messages.append("Tie Game")

        #If player one has a better hand than player (Done by comparing indexes of the 
        #type of hand from the HAND_TYPES tuple).
        if (self.hands[Game.PLAYER_ONE].get_hand_types().index(evaluate_dict[Game.PLAYER_ONE][0]) <
             self.hands[Game.PLAYER_TWO].get_hand_types().index(evaluate_dict[Game.PLAYER_TWO][0])):
             message = 0 #Index 0 of messages will print player one won
        
        #If player two has a better hand than player (Done by comparing indexes of the 
        #type of hand from the HAND_TYPES tuple).
        elif (self.hands[Game.PLAYER_ONE].get_hand_types().index(evaluate_dict[Game.PLAYER_ONE][0]) >
             self.hands[Game.PLAYER_TWO].get_hand_types().index(evaluate_dict[Game.PLAYER_TWO][0])):
            message = 1 #Index 1 of messages will print player two won

        #If player one and two have the exact same type of hand, then enter tie breaking protocols.
        else:
            #If the important cards of player one's hands is higher than the important cards of player
            #two's hand.
            if ((evaluate_dict[Game.PLAYER_ONE][1][0]) > (evaluate_dict[Game.PLAYER_TWO][1][0])):
                message = 0 #Index 0 of messages will print player one won

            #If the important cards of player two's hands is higher than the important cards of player
            #ones's hand.
            elif ((evaluate_dict[Game.PLAYER_ONE][1][0]) < (evaluate_dict[Game.PLAYER_TWO][1][0])):
                message = 1 #Index 1 of messages will print player two won

        print("******************************************************************************************")
        #Prints a message to indicate who won. If message was never reassigned, it would be the default value
        #of 2, which would print that the game has tied.
        print (messages[message])

if (__name__ == "__main__"):

    
    players = ["Ashwin", "Sanchaai"]
    poker = Game(players)
    poker.deal()
    poker.evaluate()
    