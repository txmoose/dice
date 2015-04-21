#!/usr/bin/env python3

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
