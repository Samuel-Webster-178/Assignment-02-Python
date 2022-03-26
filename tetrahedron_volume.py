#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the volume of a tetrahedron
#     with inputted edge length


import math


def main():
    # I calculate the volume of a tetrahedron

    # input
    edge_length = int(input("Input edge length of tetrahedron in cm: "))

    # process
    volume = edge_length**3 / (6 * math.sqrt(2))

    # output
    print("The volume is {} cm³.".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
