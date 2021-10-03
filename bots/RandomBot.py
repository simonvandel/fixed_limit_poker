"""Random player"""
import random
from typing import Sequence

from bots.BotInterface import BotInterface
from environment.Constants import Action
from environment.Observation import Observation


class RandomBot(BotInterface):
    """Mandatory class with the player methods"""

    def __init__(self, name="nc_random"):
        super().__init__(name=name)


    def act(self, action_space:Sequence[Action], observation:Observation) -> Action:  # pylint: disable=no-self-use
        """Mandatory method that calculates the move based on the observation array and the action space."""
        _ = observation  # not using the observation for random decision

        action = random.choice(action_space)
        return action