#!/usr/bin/env python3

import argparse
import random
import sys
import re


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

def ensure_input(dice_req):
    dice_good = []

    for die in dice_req:
        good_format = re.match('\d+d\d+', die)

        if good_format:
            dice_good.append(die)
        else:
            print('{} is improperly formatted.'.format(die))

    if dice_good:
        return dice_good
    else:
        sys.exit('All input was improperly formatted.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple dice roller')
    parser.add_argument('dice', nargs='+',
                        help='Number and Type of Dice in the form NdX')
    args = parser.parse_args()

    full_hand(ensure_input(args.dice))
