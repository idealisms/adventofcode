import collections
import copy
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
enemy_hp, enemy_damage = [int(n) for n in re.findall(r'\d+', inp, re.M)]

PLAYER_TURN, ENEMY_TURN = 0, 1
GameState = collections.namedtuple(
  'GameState',
  ['turn', 'player_hp', 'player_mana', 'mana_spent', 'enemy_hp',
   'shield_turns', 'poison_turns', 'recharge_turns'])
INITIAL_STATE = GameState(PLAYER_TURN, 50, 500, 0, enemy_hp, 0, 0, 0)
# Test case: suppose the player has 10 hit points and 250 mana, and
# that the boss has 13 (test case2: 14) hit points and 8 damage
# INITIAL_STATE = GameState(PLAYER_TURN, 10, 250, 0, 14, 0, 0, 0)

PLAYER_LOSES = 10**7
mem = {}
PART = 1
def solve(state):
  # print(state)
  if state.player_hp <= 0:
    return PLAYER_LOSES
  if state.enemy_hp <= 0:
    return state.mana_spent
  # Player loses if they can't cast a spell.
  if state.turn == PLAYER_TURN and state.player_mana < 53:
    return PLAYER_LOSES

  if state in mem:
    return mem[state]

  if state.turn == ENEMY_TURN:
    # Poison damage happens before the boss can attack.
    if state.enemy_hp <= 3 and state.poison_turns > 0:
      return state.mana_spent
    return solve(GameState(
      1 - state.turn,
      state.player_hp - max(1, enemy_damage -7 if state.shield_turns >= 1 else enemy_damage),
      state.player_mana + (101 if state.recharge_turns >= 1 else 0),
      state.mana_spent,
      state.enemy_hp - (3 if state.poison_turns >= 1 else 0),
      max(0, state.shield_turns - 1),
      max(0, state.poison_turns - 1),
      max(0, state.recharge_turns - 1),
    ))
  else:
    if PART == 2:
      if state.player_hp == 1:
        return PLAYER_LOSES

    # Cast Magic Missile
    best = solve(GameState(
      1 - state.turn,
      state.player_hp - (1 if PART == 2 else 0),
      state.player_mana - 53 + (101 if state.recharge_turns >= 1 else 0),
      state.mana_spent + 53,
      state.enemy_hp - 4 - (3 if state.poison_turns >= 1 else 0),
      max(0, state.shield_turns - 1),
      max(0, state.poison_turns - 1),
      max(0, state.recharge_turns - 1),
    ))
    # Cast Drain
    best = min(best, solve(GameState(
      1 - state.turn,
      state.player_hp + 2 - (1 if PART == 2 else 0),
      state.player_mana - 73 + (101 if state.recharge_turns >= 1 else 0),
      state.mana_spent + 73,
      state.enemy_hp - 2 - (3 if state.poison_turns >= 1 else 0),
      max(0, state.shield_turns - 1),
      max(0, state.poison_turns - 1),
      max(0, state.recharge_turns - 1),
    )))
    # Cast Shield
    if state.shield_turns <= 1:
      best = min(best, solve(GameState(
        1 - state.turn,
        state.player_hp - (1 if PART == 2 else 0),
        state.player_mana - 113 + (101 if state.recharge_turns >= 1 else 0),
        state.mana_spent + 113,
        state.enemy_hp - (3 if state.poison_turns >= 1 else 0),
        6,
        max(0, state.poison_turns - 1),
        max(0, state.recharge_turns - 1),
      )))
    # Cast Poison
    if state.poison_turns <= 1:
      best = min(best, solve(GameState(
        1 - state.turn,
        state.player_hp - (1 if PART == 2 else 0),
        state.player_mana - 173 + (101 if state.recharge_turns >= 1 else 0),
        state.mana_spent + 173,
        state.enemy_hp - (3 if state.poison_turns >= 1 else 0),
        max(0, state.shield_turns - 1),
        6,
        max(0, state.recharge_turns - 1),
      )))
    # Cast Recharge
    if state.recharge_turns <= 1:
      best = min(best, solve(GameState(
        1 - state.turn,
        state.player_hp - (1 if PART == 2 else 0),
        state.player_mana - 229 + (101 if state.recharge_turns >= 1 else 0),
        state.mana_spent + 229,
        state.enemy_hp - (3 if state.poison_turns >= 1 else 0),
        max(0, state.shield_turns - 1),
        max(0, state.poison_turns - 1),
        5,
      )))

    mem[state] = best
    return best

print('part1:', solve(INITIAL_STATE))

PART = 2
mem = {}
print('part2:', solve(INITIAL_STATE))
