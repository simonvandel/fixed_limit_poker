from typing import Dict, List

from environment.Constants import Action, Stage


class PlayerObservation:
    name: str
    stack: int
    contribution: int
    position: int
    active: bool
    win: bool
    reward: int
    history: Dict[Stage, List[Action]]

    def __init__(self) -> None:
        self.name = ""
        self.stack = 0
        self.contribution = 0
        self.position = -1
        self.active = True
        self.win = False
        self.reward = 0
        self.history = {}
        for stage in Stage:
            self.history[stage] = []
