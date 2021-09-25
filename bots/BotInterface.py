
from typing import Sequence
from env.Constants import Action
from env.Observation import Observation


class BotInterface:

    def __init__(self, name:str, autoPlay=True):
        """Initiaization of an agent"""
        self.name = name
        self.autoPlay = autoPlay

    def act(self, action_space:Sequence[Action], observation:Observation) -> Action:
        pass

    def __str__(self) -> str:
        return self.name