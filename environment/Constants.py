from enum import Enum

RANKS = '23456789TJQKA'
SUITS = 'dchs' # '2h'

class Action(Enum):
    """Allowed actions"""
    FOLD = 0
    CHECK = 1
    CALL = 2
    RAISE = 3
    SMALL_BLIND = 4
    BIG_BLIND = 5
    
class Stage(Enum):
    PREFLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    SHOWDOWN = 4
    END_HIDDEN = 5

class HandType(Enum):
    STRAIGHTFLUSH: 0
    FOUROFAKIND: 1
    FULLHOUSE: 2
    FLUSH: 3
    STRAIGHT: 4
    THREEOFAKIND: 5
    TWOPAIR: 6
    PAIR: 7
    HIGHCARD: 8
