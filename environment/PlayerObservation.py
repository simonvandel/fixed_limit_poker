
from environment.Constants import Action, Stage
from typing import Dict, Sequence, Tuple

class PlayerObservation:
    name: str
    stack: int
    contribution: int
    position: int
    active: bool 
    history: Dict[Stage, Sequence[Action]]

    def __init__(self) -> None:
        self.name = ""
        self.stack = 0
        self.contribution = 0
        self.position = -1
        self.active = True
        self.history = {}
        for stage in Stage:
            self.history[stage] = []
