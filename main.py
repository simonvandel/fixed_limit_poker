from environment.FixedLimitPoker import FixedLimitPoker
from bots.RandomBot import Player as RandomBot
from libs.utils.preFlopRank import getRankPercent

res = getRankPercent(['As', 'Ac'])

env = FixedLimitPoker([RandomBot("player1"), RandomBot("player2")])
env.reset()
env.reset(rotatePlayers=True)
env.reset(rotatePlayers=True)
env.reset(rotatePlayers=True)
env.reset(rotatePlayers=True)
