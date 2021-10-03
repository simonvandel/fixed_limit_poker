"""Fold player"""
from environment import Observation, Action
from typing import Sequence
from bots.BotInterface import BotInterface


class FoldBot(BotInterface):

    def __init__(self, name="foldalot"):
        super().__init__(name=name)

    def act(self, action_space: Sequence[Action], observation: Observation) -> Action:
        return Action.FOLD
