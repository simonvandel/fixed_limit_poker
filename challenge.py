from collections import defaultdict
import pickle
from environment.FixedLimitPoker import FixedLimitPoker
from bots import Example1Bot, MirrorBot, RandomBot, CallBot, FoldBot
import itertools
import math
import time
import json

PARTICIPANTS = [Example1Bot(), MirrorBot(), RandomBot(), CallBot(), FoldBot()]
TOTAL_ROUNDS = 100


def main():
    combinations = list(itertools.combinations(PARTICIPANTS, 2))
    rounds_for_each_pair = math.floor(TOTAL_ROUNDS / len(combinations))

    print(f"There are {len(combinations)} combinations")
    print(f"Each combination will be played: {rounds_for_each_pair} times")

    poker_rooms = [FixedLimitPoker(c) for c in combinations]
    stats = defaultdict(lambda: 0)

    start_time = time.time()
    for room in poker_rooms:
        print(f"Pairing {' vs. '.join([p.bot.name for p in room.players])}")
        for _ in range(rounds_for_each_pair):
            room.reset(rotatePlayers=True)
            for p in room.players:
                stats[p.bot.name] += p.reward

        print(json.dumps(stats, ensure_ascii=True, sort_keys=True))

    duration = time.time() - start_time
    rounds = rounds_for_each_pair * len(combinations)
    duration_pr_sim = round(duration/rounds, 5)
    print(f"-----------------------------------------")
    print(f"Simulation took {duration_pr_sim} seconds pr. round")
    print(f"--- {round(duration, 2)} seconds ---")

    ts = round(time.time())
    with open(f"./results/challenge-{ts}-{'-'.join(p.name for p in PARTICIPANTS)}.pckl", 'wb') as file:
        pickle.dump(json.dumps(stats), file)


main()
