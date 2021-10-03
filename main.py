import asyncio

from bots import Example1Bot
from environment.FixedLimitPoker import FixedLimitPoker
from environment.observers.LoggingObserver import LoggingObserver
from environment.observers.WebsocketsObserver import WebsocketsObserver

ENABLE_WEBSOCKETS = False


async def main():
    observers = [LoggingObserver()]
    if ENABLE_WEBSOCKETS:
        observers.append(WebsocketsObserver())
    env = FixedLimitPoker(
        [Example1Bot("player1"), Example1Bot("player2")], observers=observers)
    env.reset()
    env.reset(rotatePlayers=True)
    env.reset(rotatePlayers=True)
    env.reset(rotatePlayers=True)
    env.reset(rotatePlayers=True)
    if ENABLE_WEBSOCKETS:
        observers[-1].run_to_completion()

asyncio.run(main())
