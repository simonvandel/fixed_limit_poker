from unittest import TestCase
from environment.Constants import SUITS, HandType
from utils import handValue
import time

class TestUtils(TestCase):

    def testPercentValueAces(self):
        hand = ['As', 'Ah']
        val, _ = handValue.getHandPercent(hand)
        self.assertTrue(val < .1)

    def testSuitCount(self):
        board = ['As', '3s', 'Kh', '2d', 'Kc']
        hand = ['7s', 'Ah']
        count, suit = handValue.getHighestSuitCount(hand, board)
        self.assertEqual(count, 3)
        self.assertEqual(suit, 's')
        count, suit = handValue.getHighestSuitCount([], board)
        self.assertEqual(count, 2)
        self.assertEqual(suit, 's')

    def testBoardHandType(self):
        board = ['As', '3s', 'Kh']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.HIGHCARD)
        board = ['As', '3s', 'Kh', '2s']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.HIGHCARD)
        board = ['As', 'As', 'Kh']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.PAIR)
        board = ['As', 'As', 'Kh', '2s']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.PAIR)
        board = ['As', 'As', 'Kh', 'Kc']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.TWOPAIR)
        board = ['As', 'As', 'Ah']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.THREEOFAKIND)
        board = ['As', 'As', 'Ah', 'Kc']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.THREEOFAKIND)
        board = ['As', 'As', 'Ah', 'Ac']
        val = handValue.getBoardHandType(board)
        self.assertEqual(val, HandType.FOUROFAKIND)
        print()
