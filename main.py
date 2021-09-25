from environment.FixedLimitPoker import FixedLimitPoker
from bots.RandomBot import Player as RandomBot


env = FixedLimitPoker([RandomBot("player1"), RandomBot("player2")])
env.reset()