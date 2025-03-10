#!/usr/bin/env python3

import random
import sys

A=random.randint(-10,10)

with open("logs.txt", "a") as log:
    log.write(f"A = {A}\n")

print(A)


