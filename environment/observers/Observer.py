from typing import List

from environment.Constants import Action
from environment.observers.OmnipotentObservation import OmnipotentObservation
from environment.Player import Player


class Observer:
    def __init__(self) -> None:
        pass

    def LogNewGame(self, observation: OmnipotentObservation) -> None:
        pass

    def LogNewRound(self, observation: OmnipotentObservation) -> None:
        pass

    def LogPlayerAction(self, observation: OmnipotentObservation, player: Player, action: Action) -> None:
        pass

    def LogGameOver(self, observation: OmnipotentObservation) -> None:
        pass
