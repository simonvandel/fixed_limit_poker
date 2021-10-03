from typing import List

from pyfancy.pyfancy import pyfancy

from environment import Player
from environment.Constants import Action
from environment.observers.Observer import Observer
from environment.observers.OmnipotentObservation import OmnipotentObservation


class LoggingObserver(Observer):
    def __init__(self) -> None:
        pass

    def LogNewGame(self,observation: OmnipotentObservation) -> None:
        print()
        print()
        print("### NEW HAND ###")
        print()
        print(f"{observation.players[0].name}: Post Small Blind of {observation.players[0].contribution}")
        print(f"{observation.players[1].name}: Post Big Blind of {observation.players[1].contribution}")
        print(observation)
        

    def LogNewRound(self,observation: OmnipotentObservation) -> None:
        print(observation)

    def LogPlayerAction(self, observation: OmnipotentObservation, player: Player, action: Action) -> None:
        actionText = f"{player.bot.name}: {str(action)}"
        actionStr = actionText
        if action == Action.FOLD:
            actionStr = pyfancy().red(actionText).get()
        elif action == Action.CALL:
            actionStr = pyfancy().yellow(actionText + " " + str(player.contribution)).get()
        elif action == Action.RAISE:
            actionStr = pyfancy().cyan(actionText + " to " + str(player.contribution)).get()
        elif action == Action.CHECK:
            actionStr = pyfancy().green(actionText).get()
        else:
            print("Unexpected!")

        print(f"{actionStr:<40} | {self.getPotsStr(observation)}")

    def LogGameOver(self, observation: OmnipotentObservation) -> None:
        for player in observation.players:
            if player.win:
                pyfancy().green(
                    f"Winner: {player.name} | Amount: {player.reward}").output()

    def getPotsStr(self, observation: OmnipotentObservation) -> str:
        pots_str = f"TotalPot: {observation.totalPot:>3} StagePot: {observation.stagePot:>3}"
        return pyfancy().green(pots_str).get()
