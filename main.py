import asyncio
from environment.FixedLimitPoker import FixedLimitPoker
from bots.Example1Bot import Player as ExampleBot
from environment.observers.LoggingObserver import LoggingObserver
from environment.observers.WebsocketsObserver import WebsocketsObserver


async def main():
    obs = WebsocketsObserver()
    env = FixedLimitPoker(
        [ExampleBot("player1"), ExampleBot("player2")], observers=[obs, LoggingObserver()])
    env.reset()
    env.reset(rotatePlayers=True)
    env.reset(rotatePlayers=True)
    env.reset(rotatePlayers=True)
    env.reset(rotatePlayers=True)
    obs.run_to_completion()

asyncio.run(main())
