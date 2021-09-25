"""Random player"""
from bots.BotInterface import BotInterface
from env.Constants import Action
from env.Observation import Observation
import random
from typing import Sequence



class Player(BotInterface):
    """Mandatory class with the player methods"""

    def __init__(self, name="nc_random"):
        super().__init__(name=name)


    def act(self, action_space:Sequence[Action], observation:Observation) -> Action:  # pylint: disable=no-self-use
        """Mandatory method that calculates the move based on the observation array and the action space."""
        _ = observation  # not using the observation for random decision

        action = random.choice(action_space)
        return action