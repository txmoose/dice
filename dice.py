#!/usr/bin/env python

import argparse
import random


def roll(crit):
    return random.randint(1, crit)


def dice(cnt, crit):
    faces = [0]
    for x in range(0, cnt):
        face = roll(crit)
        faces[0] += face
        faces.append(face)

    print("The roll is {}".format(faces[1:]))

    if len(faces) > 2:
        print("The total is {}".format(faces[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple dice roller')
    parser.add_argument('dice', type=str,
                        help='Number and Type of Dice in the form NdX')
    args = parser.parse_args()

    (cnt, crit) = (args.dice.split('d'))

    dice(int(cnt), int(crit))
