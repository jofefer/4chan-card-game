import csv
import random

DEBUG = False
DIR_CARDS = "C:\\Users\\jfemeniafe001\\Documents\\Python Scripts\\github\\4chan-card-game\\venv\\csv\\listado_cartas.csv"


class Card:
    def __init__(self, id, type_card, name, description, effect_in_turn, debug = DEBUG):
        self.id = id
        self.type_card = type_card
        self.name = name
        self.description = description
        self.effect_in_turn = effect_in_turn
        if debug:
            print("creada la carta, ", id)

    def __str__(self):
        return 'Card({0},  {1}, "{2}", "{3}", {4})'.format(self.id, self.type_card, self.name, self.description, self.effect_in_turn)


class Deck:
    def __init__(self, DIR_CARDS= DIR_CARDS):
        self.deck = []

        with open(DIR_CARDS, 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                self.deck.append(Card(*row))

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

    def play(self):
        turnos = 3
        turno = 0
        while turnos > 0:
            if len(self.deck)== 0:
                print("END, no more cards")
                break
            print("-----------------------------------------")
            actual_player = self.players[turno % len(self.players)]

            actual_player.addCard(self.deck.drawCard())
            print("Player {0}, choose one of your cards:".format(actual_player.name))
            actual_player.showCards()

            turnos -= 1



g1 = Game([["Pepe","male"],["Manoli","female"]])
g1.play()
