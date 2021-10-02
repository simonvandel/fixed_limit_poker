from environment.FixedLimitPoker import FixedLimitPoker
from environment.observers.LoggingObserver import LoggingObserver
from environment.observers.WebsocketsObserver import WebsocketsObserver
from bots import Example1Bot, MirrorBot, RandomBot, CallBot, FoldBot
import itertools
import math

PARTICIPANTS = [Example1Bot(), MirrorBot(), RandomBot(), CallBot(), FoldBot()]
TOTAL_ROUNDS = 1000


def main():
    combinations = list(itertools.combinations(PARTICIPANTS, 2))
    rounds_for_each_pair = math.floor(TOTAL_ROUNDS / len(combinations))

    print(f"There are {len(combinations)} combinations")
    print(f"Each combination will be played: {rounds_for_each_pair} times")

    poker_rooms = [FixedLimitPoker(c) for c in combinations]
    stats = dict()

    for room in poker_rooms:
        print(f"Pairing {', '.join([p.bot.name for p in room.players])}")
        for _ in range(rounds_for_each_pair):
            room.reset(rotatePlayers=True)
            for p in room.players:
                if p.bot.name not in stats:
                    stats[p.bot.name] = 0
                stats[p.bot.name] += p.reward

        print(stats)


main()
