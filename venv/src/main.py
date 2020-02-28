import csv
import random

DEBUG = False
if DEBUG:
    print("............DEBUG MODE............")

DIR_CARDS = "C:\\Users\\jfemeniafe001\\Documents\\Python Scripts\\github\\4chan-card-game\\venv\\csv\\listado_cartas.csv"

# TODO : implement this class to extract all info
# ocr url ---> https://ocr.space/OCRAPI
class Ocr:
    def convert_all(self):
        pass

class Card:
    #TODO add card IMG
    def __init__(self, id, type_card, name, description, effect, debug = DEBUG):
        """ effect_in_turn:
        0 - to yourself
        1 - pick someone
        """
        self.id = id
        self.type_card = type_card
        self.name = name
        self.description = description
        self.effect = effect
        if debug:
            print("creada la carta, ", id)

    def __str__(self):
        return 'Card({0},  {1}, "{2}", "{3}", {4})'.format(self.id, self.type_card, self.name, self.description, self.effect)
    
    #TODO __desc(self)__


class Deck:
    def __init__(self, DIR_CARDS= DIR_CARDS, debug= DEBUG):
        self.deck = []

        with open(DIR_CARDS, 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                self.deck.append(Card(*row))

        if debug:
            print("THE CARDS ARE:")
            self.showCards()

    def __len__(self):
        return len(self.deck)

    def ranShuffle(self):
        self.deck = sorted(self.deck, key= lambda x: random.random())

    def showCards(self):
        for card in self.deck:
            print(card)

    def drawCard(self):
        self.ranShuffle()
        return self.deck.pop()


class Player:
    num_players = 0
    PLAYERS_MAX = 10

    def __init__(self,name, sex):
        self.id = Player.num_players
        self.name = name
        self.sex = sex
        self.owned_cards = []
        Player.num_players += 1

    def addCard(self, card):
        if isinstance(card, Card):
            self.owned_cards.append((card))
            print("card added")
        else:
            raise ValueError("You should add a card")

    def showCards(self):
        for card in self.owned_cards:
            print(card)

class Game:
    def __init__(self, playersList):
        self.deck = Deck()
        self.players = [Player(*x) for x in playersList]

    # TODO implement addPlayer
    def addPlayer(self):
        pass

    def play(self):
        turns = 8
        turn = 0
        if turns == 0:
            print("END OF THE GAME")
        while turns > 0:
            if len(self.deck) == 0:
                print("GAME OVER    no more cards")
                break

            print("-----------------------------------------")
            player_tourn = turn % len(self.players)
            actual_player = self.players[player_tourn]

            new_card = self.deck.drawCard()

            print("{0} tourn ".format(actual_player.name))
            if int(new_card.type_card) == 0:
                print("ACTION!!! Do what it says:\n ----> \t",new_card.description)
            elif int(new_card.type_card) == 1:
                print("You have drow an INSTANT card")
                actual_player.addCard(new_card)
            elif int(new_card.type_card) == 2:
                print("MANDATORY: \n ---->\t",new_card.description)
            else:
                print("STATUS")
                actual_player.addCard(new_card)

            menu = True
            while menu:
                print("\nYour curent cards are:")
                print(actual_player.showCards())
                print("\nWhat do you want to do? \n"
                      "\t1- End your turn \n"
                      "\t2- SOME OPTION")
                option = int(input())
                if option == 1:
                    menu = False
                    continue
            turns -= 1
            turn += 1



g1 = Game([["Pepe","male"],["Manoli","female"], ["player3", "transexual"]])
g1.play()
print("")
