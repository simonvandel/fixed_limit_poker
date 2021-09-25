from random import shuffle as rshuffle
from typing import Sequence
from environment.Constants import RANKS, SUITS

class Deck:
    
    _FULL_DECK: Sequence[str] = []

    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.cards = Deck.GetFullDeck()
        rshuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def drawMultiple(self, n=1):
        cards: list[str] = []
        for _ in range(n):
            cards.append(self.draw())
        return cards

    def __str__(self):
        return print(self.cards)

    @staticmethod
    def GetFullDeck():
        if Deck._FULL_DECK:
            return list(Deck._FULL_DECK)

        # create the standard 52 card deck
        for rank in RANKS:
            for suit in SUITS:
                Deck._FULL_DECK.append(rank + suit)

        return list(Deck._FULL_DECK)