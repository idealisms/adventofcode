import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''

grid = inp.splitlines()
start_pos = (0, 1)
num_rows = len(grid)
num_cols = len(grid[0])
exit_pos = (num_rows - 1, num_cols - 2)

def is_open(nr, nc, minute):
    if (nr, nc) in (start_pos, exit_pos):
        return True
    if nr <= 0 or nc <= 0 or nr >= num_rows - 1 or nc >= num_cols - 1:
        return False
    if grid[(nr - 1 + minute) % (num_rows - 2) + 1][nc] == '^':
        return False
    if grid[(nr - 1 - minute) % (num_rows - 2) + 1][nc] == 'v':
        return False
    if grid[nr][(nc - 1 + minute) % (num_cols - 2) + 1] == '<':
        return False
    if grid[nr][(nc - 1 - minute) % (num_cols - 2) + 1] == '>':
        return False
    return True

def solve(exit_pos, start_pos, start_min):
    pts = {start_pos}
    for minute in range(start_min, 999):
        # print(minute - 1, pts)
        new_pts = set()
        for pt in pts:
            for dr, dc in [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
                (0, 0),
            ]:
                nr = pt[0] + dr
                nc = pt[1] + dc
                if (nr, nc) == exit_pos:
                    return minute
                if is_open(nr, nc, minute):
                    new_pts.add((nr, nc))
        pts = new_pts

part1 = solve(exit_pos, start_pos, 1)
print(part1)
back_to_start_min = solve(start_pos, exit_pos, part1+1)
part2 = solve(exit_pos, start_pos, back_to_start_min)
print(part2)
