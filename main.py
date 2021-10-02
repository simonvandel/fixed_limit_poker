from environment.FixedLimitPoker import FixedLimitPoker
from bots.RandomBot import Player as RandomBot
from bots.Example1Bot import Player as ExampleBot
from utils.handValue import getHandType, getHandPercent

#res = getHandPercent(['Qs', '3c'], ['6d','Qh','2c'])

env = FixedLimitPoker([ExampleBot("player1"), ExampleBot("player2")])
env.reset()
env.reset(rotatePlayers=True)
env.reset(rotatePlayers=True)
env.reset(rotatePlayers=True)
env.reset(rotatePlayers=True)
