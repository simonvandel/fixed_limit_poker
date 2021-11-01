from bots import PercentBot
from bots.SimonBot import SimonBot
from environment.FixedLimitPoker import FixedLimitPoker
from environment.observers.LoggingObserver import LoggingObserver


def main():
    observers = [LoggingObserver()]
    env = FixedLimitPoker(
        [PercentBot(), SimonBot()], observers=observers)
    env.reset()
    # env.reset(rotatePlayers=True)
    # env.reset(rotatePlayers=True)
    # env.reset(rotatePlayers=True)
    # env.reset(rotatePlayers=True)


main()
