from typing import List
from environment.Constants import Action
from environment.Player import Player
from environment.observers.OmnipotentObservation import OmnipotentObservation


class Observer:
    def __init__(self) -> None:
        pass

    def LogNewGame(observation: OmnipotentObservation) -> None:
        pass

    def LogNewRound(observation: OmnipotentObservation) -> None:
        pass

    def LogPlayerAction(observation: OmnipotentObservation, player: Player, action: Action) -> None:
        pass

    def LogGameOver(observation: OmnipotentObservation) -> None:
        pass
