"""empty bot player"""
from typing import Sequence
from bots.BotInterface import BotInterface


class EmptyBot(BotInterface):

    def __init__(self, name="empty"):
        super().__init__(name=name, autoPlay=False)
