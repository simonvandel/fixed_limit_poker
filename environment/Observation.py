
from environment.PlayerObservation import PlayerObservation
from environment.Constants import Stage
from typing import Sequence


class Observation:
    boardCards: Sequence[str]
    stage: Stage
    totalPot: int
    stagePot: int
    players: Sequence[PlayerObservation]
    myPosition: int
    myHand: Sequence[str]

    def __init__(self) -> None:
        self.boardCards = []
        self.players = []
        self.stage = Stage.PREFLOP
        self.totalPot = 0
        self.stagePot = 0
        self.myPosition = 0
        self.myHand = []
