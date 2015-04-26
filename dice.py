#!/usr/bin/env python3

import argparse
import random


def roll(critical_roll):
    return random.randint(1, critical_roll)

def full_hand(die_list):
    total = [0]
    for die in die_list:
        (num_dice, critical_roll) = die.split('d')
        (num_dice, critical_roll) = (int(num_dice), int(critical_roll))

        for y in range(0, num_dice):
            face = roll(critical_roll)
            total[0] += face
            total.append(face)

    print("The roll is {}".format(total[1:]))

    if len(total) > 2:
        print("The total is {}".format(total[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple dice roller')
    parser.add_argument('dice', nargs='+',
                        help='Number and Type of Dice in the form NdX')
    args = parser.parse_args()

    full_hand(args.dice)
