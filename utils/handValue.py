from typing import List
import pickle
from utils.deuces.card import Card

from utils.deuces.evaluator import Evaluator

def _getPreflopHandType(hand: List[str]) -> str:
    hand = sorted(hand, key=lambda x: x[0])

    if hand[0][0] == hand[1][0]:
        return hand[0][0] + hand[1][0]
    elif hand[0][1] == hand[1][1]:
        return hand[0][0] + hand[1][0] + 's'
    else:
        return hand[0][0] + hand[1][0] + 'o'

def getHandPercent(hand: List[str], board: List[str] = []) -> float:
    if len(board) == 0:
        with open('./utils/preflopHandRankings.pckl', 'rb') as rankingsFile:
            rankings = pickle.load(rankingsFile)
            preflopHandType = _getPreflopHandType(hand)
            return rankings[preflopHandType]
    else:
        evaluator = Evaluator()
        d_hand = [Card().new(c) for c in hand]
        d_board = [Card().new(c) for c in board]
        rank = evaluator.evaluate(d_hand, d_board)
        percentage = evaluator.get_five_card_rank_percentage(rank)  # higher better here
        return percentage * 100


def getHandType(hand: List[str], board: List[str] = []) -> str:
    if len(board) == 0:
        return _getPreflopHandType(hand)
    else:    
        d_hand = [Card().new(c) for c in hand]
        d_board = [Card().new(c) for c in board]
        evaluator = Evaluator()
        return evaluator.class_to_string(evaluator.get_rank_class(evaluator.evaluate(d_hand, d_board)))
