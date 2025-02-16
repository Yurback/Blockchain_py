# First realization
# import argparse

# #pars = argparse.ArgumentParser()

# pars.add_argument("heads", type=int)
# pars.add_argument("legs", type=int)

# args = pars.parse_args()

# Second realization
import sys

args = sys.argv[1:]


def animal(g, n):
    a = []
    for i in range(g):
        j = i + 1
        if j * 2 + (g - j) * 4 == n:
            a = [j, g - j]
    return a


a = animal(int(args[0]), int(args[1]))

print(a)
