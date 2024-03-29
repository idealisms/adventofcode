import abc
import collections
import itertools
import math
import re
from typing import AsyncIterable

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = '''--- scanner 0 ---
# 404,-588,-901
# 528,-643,409
# -838,591,734
# 390,-675,-793
# -537,-823,-458
# -485,-357,347
# -345,-311,381
# -661,-816,-575
# -876,649,763
# -618,-824,-621
# 553,345,-567
# 474,580,667
# -447,-329,318
# -584,868,-557
# 544,-627,-890
# 564,392,-477
# 455,729,728
# -892,524,684
# -689,845,-530
# 423,-701,434
# 7,-33,-71
# 630,319,-379
# 443,580,662
# -789,900,-551
# 459,-707,401

# --- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390

# --- scanner 2 ---
# 649,640,665
# 682,-795,504
# -784,533,-524
# -644,584,-595
# -588,-843,648
# -30,6,44
# -674,560,763
# 500,723,-460
# 609,671,-379
# -555,-800,653
# -675,-892,-343
# 697,-426,-610
# 578,704,681
# 493,664,-388
# -671,-858,530
# -667,343,800
# 571,-461,-707
# -138,-166,112
# -889,563,-600
# 646,-828,498
# 640,759,510
# -630,509,768
# -681,-892,-333
# 673,-379,-804
# -742,-814,-386
# 577,-820,562

# --- scanner 3 ---
# -589,542,597
# 605,-692,669
# -500,565,-823
# -660,373,557
# -458,-679,-417
# -488,449,543
# -626,468,-788
# 338,-750,-386
# 528,-832,-391
# 562,-778,733
# -938,-730,414
# 543,643,-506
# -524,371,-870
# 407,773,750
# -104,29,83
# 378,-903,-323
# -778,-728,485
# 426,699,580
# -438,-605,-362
# -469,-447,-387
# 509,732,623
# 647,635,-688
# -868,-804,481
# 614,-800,639
# 595,780,-596

# --- scanner 4 ---
# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14'''


scanners = []
for scanner_inp in inp.split('\n\n'):
    points = []
    for line in scanner_inp.splitlines()[1:]:
        points.append(tuple(map(int, line.split(','))))
    scanners.append(points)

def getRotations(points):
    axes = list(zip(*points))
    rotations = []
    directions = [
        # +/- and facing
        [1, 1, 1],
        [-1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [1, 1, -1],
        [-1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1],
    ]
    for order in itertools.permutations([0,1,2]):
        for direction in directions:
            rotations.append(
                list(zip(*[
                    [direction[0] * n for n in axes[order[0]]],
                    [direction[1] * n for n in axes[order[1]]],
                    [direction[2] * n for n in axes[order[2]]],
                ]))
            )
    return rotations

# x,y
# -y,x
# -x,-y
# y,-x
    # print(len(set(list(zip(*rotations))[0])))

deltas = []
def findBeaconsOverlap(srot1, srot2):
    global deltas
    setPts1 = set(srot1)
    for pt1 in srot1:
        for pt2 in srot2:
            # print(pt1, pt2)
            delta = [pt2[0] - pt1[0], pt2[1] - pt1[1], pt2[2] - pt1[2]]
            translated = [
                (pt[0] - delta[0], pt[1] - delta[1], pt[2] - delta[2]) for pt in srot2
            ]
            # print(setPts1)
            # print(pt1, pt2, delta)
            # print(translated)
            beacons = setPts1.intersection(set(translated))
            if len(beacons) >= 12:
                print('matched', delta)
                deltas.append(delta)
                # print(beacons)
                for i, pt in enumerate(srot2):
                    srot2[:] = translated
                return True

def findMatchingBeacons(base_scanner, scanner_rots):
    for rotation in getRotations(scanner_rots):
        if findBeaconsOverlap(base_scanner, rotation):
            scanner_rots[:] = rotation
            return True

matched = [0] * len(scanners)
matched[0] = 1
new_matched = [0]
beacons = set()
while sum(matched) != len(scanners):
    base_scanner_idx = new_matched.pop()
    base_scanner = scanners[base_scanner_idx]
    for i, scanner in enumerate(scanners):
        if not matched[i]:
            if findMatchingBeacons(base_scanner, scanner):
                matched[i] = True
                new_matched.append(i)
                print('matched {} to {}\n'.format(i, base_scanner_idx))

beacons = set()
for scanner in scanners:
    beacons.update(scanner)
print('part1:', len(beacons))

def mdist(pt1, pt2):
    return (
        abs(pt1[0] - pt2[0]) +
        abs(pt1[1] - pt2[1]) +
        abs(pt1[2] - pt2[2]))

part2 = 0
for i, pt in enumerate(deltas):
    for pt2 in deltas[i+1:]:
        part2 = max(part2, mdist(pt, pt2))
print(part2)
