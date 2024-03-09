import random

t_rang = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
dict_suits = {'hearts': '♥️', 'spades': '♠️', 'diamonds': '♦️', 'clubs': '♣️'}


class Card:
    def __init__(self, rang, suit):
        self.rang = rang
        self.suit = suit

    def __str__(self):
        return self.rang+dict_suits[self.suit]


class Deck:
    def __init__(self):
        self.deck = [Card(rang, suit) for rang in t_rang for suit in dict_suits]

    def __str__(self):
        return str(self.deck)

    def get_card(self):
        return self.deck.pop(random.randint(0, len(self.deck)))


d = Deck()
print([str(d.get_card()) for _ in range(10)])
print(len(d.deck))
