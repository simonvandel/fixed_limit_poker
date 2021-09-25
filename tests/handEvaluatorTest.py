
from environment.Card import Card
from environment.HandEvaluator import get_winner

player1Cards = [Card('Ah'), Card('As')]
player2Cards = [Card('3h'), Card('4h')]
boardCards = [Card('Ad'),Card('2d'),Card('7s'),Card('Td'),Card('Ks')]

get_winner([player1Cards, player2Cards], boardCards)