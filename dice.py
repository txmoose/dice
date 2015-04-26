#!/usr/bin/env python3

import argparse
import random


class Dice:
    def __init__(self, name):
        self.name = name

    def roll(self, critical_roll):
        return random.randint(1, critical_roll)

    def full_hand(self, die_list):
        total = [0]
        for die in die_list:
            (num_dice, critical_roll) = die.split('d')
            (num_dice, critical_roll) = (int(num_dice), int(critical_roll))

            for y in range(0, num_dice):
                face = self.roll(critical_roll)
                total[0] += face
                total.append(face)

        print("{}'s roll is {}".format(self.name.capitalize(), total[1:]))

        if len(total) > 2:
            print("{}'s total is {}".format(self.name.capitalize(), total[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple dice roller')
    parser.add_argument('dice', nargs='+',
                        help='Number and Type of Dice in the form NdX')
    parser.add_argument('-n', '--name', help='Name of roller', dest='name',
                        default='Player', type=str)
    args = parser.parse_args()

    dice = Dice(args.name)

    dice.full_hand(args.dice)
