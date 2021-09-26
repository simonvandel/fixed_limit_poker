from typing import List
from pyfancy.pyfancy import pyfancy
from environment import Player
from environment.observers.OmnipotentObservation import OmnipotentObservation
from environment.observers.Observer import Observer
from environment.Constants import Action


class LoggingObserver(Observer):
    def __init__(self) -> None:
        pass

    def LogNewGame(observation: OmnipotentObservation) -> None:
        print(observation)

    def LogNewRound(observation: OmnipotentObservation) -> None:
        print(observation)

    def LogPlayerAction(observation: OmnipotentObservation, player: Player, action: Action) -> None:
        text = f"{player.bot.name}: {action}"
        if action == Action.FOLD:
            pyfancy().red(text).output()
        elif action == Action.CALL:
            pyfancy().yellow(text).output()
        elif action == Action.RAISE:
            pyfancy().cyan(text).output()
        elif action == Action.CHECK:
            pyfancy().green(text).output()
        else:
            print("Unexpected!")

    def LogGameOver(observation: OmnipotentObservation, winnerPositions: List[int]) -> None:
        for i in winnerPositions:
            pyfancy().green(f"Winner: {observation.players[i].name}").output()
