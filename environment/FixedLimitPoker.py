from copy import deepcopy
from libs.deuces.evaluator import Evaluator
from libs.deuces.card import Card
from environment.PlayerObservation import PlayerObservation
from environment.Deck import Deck
from environment.Player import Player
from environment.Constants import Action, Stage
from typing import List, Tuple
from environment.Observation import Observation

class FixedLimitPoker:
    boardCards: List[str]
    stage: Stage
    totalPot: int
    stagePot: int
    players: List[Player]
    activePlayerQueue: List[int]
    numPlayers: int
    smallBlind: int
    bigBlind: int
    stackSize: int
    actionSpace: List[Action]
    deck: Deck
    raiseCount: int
    evaluator: Evaluator

    def __init__(self, players: List[Player], smallBlind=5, bigBlind=10, stackSize = 1000) -> None:
        self.players = [Player(player) for player in players]
        self.numPlayers = len(self.players)
        self.smallBlind = smallBlind
        self.bigBlind = bigBlind
        self.stackSize = stackSize
        self.evaluator = Evaluator()

    def reset(self) -> Tuple[List[Action],Observation,int,bool]:    
        self.boardCards = []
        self.activePlayerQueue = []
        self.stage = Stage.PREFLOP
        self.totalPot = 0
        self.stagePot = 0
        self.raiseCount = 0
        self.actionSpace = [Action.FOLD, Action.CALL, Action.RAISE]
        self.rotatePlayers()
        for i in range(self.numPlayers):
            self.players[i].reset(stack=self.stackSize, position=i)
            self.activePlayerQueue.append(i)
        self.postBlinds()
        self.deck = Deck()
        self.dealHands()
        if self.getCurrentPlayer().isAutoPlayer():
            action = self.getAutoPlayerMove()
            self.step(action)
        return (self.actionSpace, self.getObservation(), 0, False)
    
    def rotatePlayers(self) -> None:
        self.players.append(self.players.pop())

    def step(self, action:Action) -> Tuple[List[Action],Observation,int,bool] :
        if not action in self.actionSpace:
            action = self.checkFold()
        self.executeStep(action)
        self.nextPlayer(action)
        self.updateActionSpace()
        if self.isRoundOver():
            if len(self.activePlayerQueue) == 1:
                self.stage = Stage.END_HIDDEN
            else:
                self.stage = Stage(self.stage.value+1)
            self.newRound()
        
        if self.stage == Stage.END_HIDDEN:
            for player in self.players:
                if not player.isAutoPlayer():
                    return ([], self.getObservation(), self.getReward(player, player.active), True)
            return ([], None, 0, True)

        if self.stage.SHOWDOWN:
            winnerPositions = self.getWinnerPositions()
            for player in self.players:
                if not player.isAutoPlayer():
                    return ([], self.getObservation(), self.getReward(player, player.position in winnerPositions, len(winnerPositions)), True)
            return ([], None, 0, True)
        
        if self.getCurrentPlayer().isAutoPlayer():
            self.step(self.getAutoPlayerMove())
        else:
            return (self.actionSpace, self.getObservation(), 0, False)

    def getReward(self, player:Player, win:bool, numWinners:int = 1):
        wagered = (self.stackSize - player.stack)
        if win:
            return int(self.totalPot / numWinners) - wagered
        else:
            return wagered * -1

    def getWinnerPositions(self):
        winnerVal = 0
        winners = []
        board = [Card.new(c) for c in self.boardCards]
        for i in self.activePlayerQueue:
            hand = [Card.new(c) for c in self.players[i].hand]
            val = self.evaluator.evaluate(board, hand)
            if val > winnerVal:
                winnerVal = val
                winners = [i]
            elif val == winnerVal:
                winners.append(i)
        return winners
        

    def newRound(self) -> None:
        self.activePlayerQueue = sorted(self.activePlayerQueue)
        self.stagePot = 0
        self.raiseCount = 0
        for i in self.activePlayerQueue:
            self.players[i].contribution = 0
        if self.stage == Stage.FLOP:
            self.boardCards = self.deck.drawMultiple(3)
        elif self.stage.value <= Stage.RIVER.value:
            self.boardCards.append(self.deck.draw())
        
    def updateActionSpace(self) -> None:
        actions = []
        if self.raiseCount == 0 and (self.stage != Stage.PREFLOP or            # after first round no raisers
            (self.stage == Stage.PREFLOP and self.activePlayerQueue[0] == 1)): # first round all call/fold to big blind
                actions.append(Action.CHECK)
        else:
            actions.append(Action.FOLD)
            if self.getCurrentPlayer().stack >= self.getCallAmount():
                actions.append(Action.CALL)

        if self.raiseCount != 4 and self.getCurrentPlayer().stack > self.getCallAmount():
            actions.append(Action.RAISE)
            
        self.actionSpace = actions


    def nextPlayer(self, action:Action) -> None:
        if action == Action.FOLD:
            self.activePlayerQueue.pop()
        else:
            self.activePlayerQueue.append(self.activePlayerQueue.pop())
            

    def executeStep(self, action:Action) -> None:
        currentPlayer = self.getCurrentPlayer()
        currentPlayer.history[self.stage].append(action)
        if action == Action.CHECK:
            pass
        elif action == Action.FOLD:
            currentPlayer.active = False
        elif action == Action.CALL:
            self.postAmount(currentPlayer, self.getCallAmount())
        elif action == Action.RAISE:
            self.raiseCount += 1
            self.postAmount(currentPlayer, min(self.getCallAmount() + self.getRaiseAmount(), currentPlayer.stack))

    def isRoundOver(self):
        if len(self.activePlayerQueue) == 1:
            return True
        if all([self.players[i].stack == 0 for i in self.activePlayerQueue]):
            return True
        if self.raiseCount > 0 and self.equalContribution():
            return True
        if self.allChecked():
            return True
        return False

    def allChecked(self) -> bool:
        for player in self.players:
            if player.active:
                hist = player.history[self.stage]
                if len(hist) == 0 or hist[-1] != Action.CHECK:
                    return False
        return True

    def equalContribution(self) -> bool:
        contributions = []
        for player in self.players:
            if player.active:
                contributions.append(player.contribution)
        return len(set(contributions)) == 1

    def executeCheckStep(self) -> None:
        currentPlayer = self.getCurrentPlayer()
        currentPlayer.history[self.stage].append(Action.CHECK)
        
    def checkFold(self) -> Action:
        if Action.CHECK in self.actionSpace:
            return Action.CHECK
        else:
            return Action.FOLD

    def getAutoPlayerMove(self) -> Action:
        return self.getCurrentPlayer().bot.act(self.actionSpace, self.getObservation())

    def getObservation(self) -> Observation:
        obs = Observation()
        obs.stage = self.stage
        obs.boardCards = list(self.boardCards)
        obs.myHand = list(self.getCurrentPlayer().hand)
        obs.myPosition = self.activePlayerQueue[0]
        obs.stagePot = self.stagePot
        obs.totalPot = self.totalPot
        obs.players = [self.getPlayerObs(player) for player in self.players]
        return obs

    def getPlayerObs(self, player: Player) -> PlayerObservation:
        playerObs = PlayerObservation()
        playerObs.stack = player.stack
        playerObs.active = player.active
        playerObs.contribution = player.contribution
        playerObs.name = player.bot.name
        playerObs.position = player.position
        playerObs.history =  deepcopy(player.history)
        return playerObs

        
    def getCurrentPlayer(self) -> Player:
        return self.players[self.activePlayerQueue[0]]

    def dealHands(self) -> None:
        for player in self.players:
            player.hand = self.deck.drawMultiple(2)

    def getCallAmount(self) -> int:
        maxContribution = max(self.players, key=lambda p: p.contribution).contribution
        return maxContribution - self.getCurrentPlayer().contribution

    def getRaiseAmount(self) -> int:
        if self.stage == Stage.PREFLOP or self.stage == Stage.FLOP:
            return self.bigBlind
        else:
            return self.bigBlind * 2

    def postBlinds(self) -> None:
        playerSmallBlind = self.players[self.activePlayerQueue[0]]
        self.postAmount(playerSmallBlind, self.smallBlind)
        self.activePlayerQueue.append(self.activePlayerQueue.pop())

        playerBigBlind = self.players[self.activePlayerQueue[0]]
        self.postAmount(playerBigBlind, self.bigBlind)
        self.activePlayerQueue.append(self.activePlayerQueue.pop())
        
    def postAmount(self, player:Player, amount:int) -> None:
        player.postAmount(amount)
        self.stagePot += amount
        self.totalPot += amount



    