import collections
import itertools
import math
import re

# Shout out to twitch.tv/LarryNY who helped spot
# an error in part2 that I was stuck on for >30min.

pos = [6, 4]
scores = [0, 0]

next_roll = 1
player = 0
while True:
    pos[player] += (next_roll+1)*3
    pos[player] %= 10
    scores[player] += 10 if pos[player] == 0 else pos[player]
    if scores[player] >= 1000:
        break
    next_roll += 3
    player = 1 - player

print(scores[1-player] * (next_roll + 2))

def distribution():
    roll_sum = collections.defaultdict(int)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                roll_sum[i+j+k] += 1
    return roll_sum

states = {
    # pos1, pos2, score1, score2: number
    (6, 4, 0, 0): 1
    # (4, 8, 0, 0): 1
}
player = 0

roll_dist = distribution()
# print(roll_dist)
done = False
turn = 1
while not done:
    print('turn', turn)
    # print(states)
    new_states = collections.defaultdict(int)
    for (pos1, pos2, score1, score2), freq in states.items():
        if score1 >= 21 or score2 >= 21:
            new_states[(pos1, pos2, score1, score2)] += freq
            continue

        for roll, new_freq in roll_dist.items():
            pos = [pos1, pos2]
            scores = [score1, score2]

            pos[player] += roll
            pos[player] %= 10
            scores[player] += 10 if pos[player] == 0 else pos[player]
            new_states[(pos[0], pos[1], scores[0], scores[1])] += freq * new_freq

    print(len(states), len(new_states), sum(new_states.values()))
    print()
    states = new_states
    
    player = 1 - player
    done = True
    for _, _, score1, score2 in states.keys():
        if score1 < 21 and score2 < 21:
            done = False
            break
    turn += 1

wins = [0, 0]
for (_, _, score1, score2), freq in states.items():
    if score1 >= 21:
        wins[0] += freq
    elif score2 >= 21:
        wins[1] += freq
    else:
        assert False, 'no one won'
print(max(wins))
