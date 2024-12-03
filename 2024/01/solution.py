#!/usr/bin/env python3
import re


def read_file():
    fname = "input.txt"
    fhandle = open(fname)
    left_locations = list()
    right_locations = list()

    for line in fhandle:
        clean_line = line.rstrip()
        locations = re.findall("[0-9]+", clean_line)
        left_locations.append(int(locations[0]))
        right_locations.append(int(locations[1]))

    return left_locations, right_locations


def puzzle_1():
    far_apart = list()
    left_locations, right_locations = read_file()
    left_locations.sort()
    right_locations.sort()

    for i in range(len(left_locations)):
        distance = left_locations[i] - right_locations[i]
        if distance < 0:
            distance *= -1
        far_apart.append(distance)

    print("Total distance:", sum(far_apart))


def puzzle_2():
    left_locations, right_locations = read_file()
    left_locations.sort()
    right_locations.sort()
    r_dic = dict()
    total = list()
    # Count the times a location appears in right list
    for r in right_locations:
        r_dic[r] = r_dic.get(r, 0) + 1

    # Multiply the location in left list with the amount of times
    # that location appears in right list
    for l in left_locations:
        t = r_dic.get(l)
        if t:
            total.append(t * l)
    print("Similarity score", sum(total))


print("***** PUZZLE 1 *****")
puzzle_1()
print("***** PUZZLE 2 *****")
puzzle_2()
