#!/usr/bin/env python3

import argparse
import random


class dice:
    def __init__(self):
        pass

    def roll(self, crit):
        return random.randint(1, crit)

    def dice(self, cnt, crit):
        faces = [0]
        for x in range(0, cnt):
            face = self.roll(crit)
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

    Dice = dice()

    (cnt, crit) = (args.dice.split('d'))

    Dice.dice(int(cnt), int(crit))
