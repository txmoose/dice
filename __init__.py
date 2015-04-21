#!/usr/bin/env python3

import argparse
from dice import Dice


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple dice roller')
    parser.add_argument('dice', type=str,
                        help='Number and Type of Dice in the form NdX')
    args = parser.parse_args()

    dice = Dice()

    (cnt, crit) = (args.dice.split('d'))

    dice.dice(int(cnt), int(crit))
