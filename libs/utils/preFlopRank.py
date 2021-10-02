from typing import List
import pickle

def getPreflopHandType(hand: List[str]) -> str:
    hand = sorted(hand, key=lambda x: x[0])

    if hand[0][0] == hand[1][0]:
        return hand[0][0] + hand[1][0]
    elif hand[0][1] == hand[1][1]:
        return hand[0][0] + hand[1][0] + 's'
    else:
        return hand[0][0] + hand[1][0] + 'o'

def getRankPercent(hand: List[str]):
    with open('./libs/utils/preflopHandRankings.pckl', 'rb') as rankingsFile:
        rankings = pickle.load(rankingsFile)
        preflopHandType = getPreflopHandType(hand)
        return rankings[preflopHandType]



