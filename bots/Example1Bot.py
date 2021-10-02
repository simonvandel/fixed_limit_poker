"""Example1 player"""
from environment.Observation import Observation
from environment.Constants import Action, HandType, Stage, RANKS
from typing import Sequence
from bots.BotInterface import BotInterface
from utils import handValue


class Example1Bot(BotInterface):

    def __init__(self, name="example1"):
        super().__init__(name=name)
        raiseCount = 0

    def act(self, action_space: Sequence[Action], observation: Observation) -> Action:
        stage = observation.stage
        if stage == Stage.PREFLOP:
            return self.getNearestAction(self.handlePreFlop(observation), action_space)
        elif stage == Stage.FLOP:
            return self.getNearestAction(self.handleFlop(observation), action_space)
        elif stage == Stage.TURN:
            return self.getNearestAction(self.handleTurn(observation), action_space)
        elif stage == Stage.RIVER:
            return self.getNearestAction(self.handleRiver(observation), action_space)

    def handlePreFlop(self, observation: Observation) -> Action:
        raiseCount = self.countRaises(observation, Stage.PREFLOP)
        handPercent = handValue.getHandPercent(observation.myHand)
        if handPercent < (40 - (10*raiseCount)):
            return Action.RAISE
        elif handPercent < (60 - (10*raiseCount)):
            return Action.CALL
        return Action.FOLD

    def handleFlop(self, observation: Observation) -> Action:
        raiseCount = self.countRaises(observation, Stage.FLOP)
        handPercent = handValue.getHandPercent(
            observation.myHand, observation.boardCards)
        if handPercent <= (60 - (10*raiseCount)):
            return Action.RAISE
        elif handPercent <= (80 - (10*raiseCount)) or self.getFlushDraw(observation) or self.getStraightDraw(observation):
            return Action.CALL
        return Action.FOLD

    def handleTurn(self, observation: Observation) -> Action:
        raiseCount = self.countRaises(observation, Stage.TURN)
        handPercent = handValue.getHandPercent(
            observation.myHand, observation.boardCards)
        if handPercent <= (50 - (10*raiseCount)):
            return Action.RAISE
        elif handPercent <= (70 - (10*raiseCount)) or self.getFlushDraw(observation) or self.getStraightDraw(observation):
            return Action.CALL
        return Action.FOLD

    def handleRiver(self, observation: Observation) -> Action:
        raiseCount = self.countRaises(observation, Stage.RIVER)
        handPercent = handValue.getHandPercent(
            observation.myHand, observation.boardCards)
        if handPercent <= (40 - (10*raiseCount)):
            return Action.RAISE
        elif handPercent <= (60 - (10*raiseCount)):
            return Action.CALL
        return Action.FOLD

    def countRaises(self, observation: Observation, stage: Stage = None) -> int:
        count = 0
        for player in observation.players:
            if not stage == None:
                count += player.history[stage].count(Action.RAISE)
            else:
                for s in Stage:
                    count += player.history[s].count(Action.RAISE)
        return count

    def getNearestAction(self, action: Action, actionSpace: Sequence[Action]) -> Action:
        while action not in actionSpace:
            if action.value == 0:
                return Action.CHECK
            action = Action(action.value-1)
        return action

    def getFlushDraw(self, observation: Observation):
        suitCounts = {}
        for c in observation.myHand:
            if c[1] in suitCounts:
                suitCounts[c[1]] += 1
                if suitCounts[c[1]] == 4:
                    print("flushdraw")
                    return True
            else:
                suitCounts[c[1]] = 0
        return False

    def getStraightDraw(self, observation: Observation):
        cardRanks = list([RANKS.index(c[0]) for c in observation.myHand])
        [cardRanks.append(RANKS.index(c[0])) for c in observation.boardCards]
        cardRanksSet = set(cardRanks)
        cardRanksSet = sorted(cardRanksSet)
        if len(cardRanksSet) < 4:
            return False
        for i in range(len(cardRanksSet)-3):
            if cardRanksSet[i] == (cardRanksSet[i+3] + 3) and cardRanksSet[i+3] != RANKS.index('A'):
                print("straightDraw")
                return True
        return False
