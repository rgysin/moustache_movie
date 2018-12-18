#!/usr/bin/env python

import math

def dist (p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def tests():
    passed = True;

    #Probably don't have to test this, but it's the thought that counts
    d = dist((0, 0), (1, 0))
    if d != 1:
        print("Failed simple test...")
        print ("(0, 0) -> (1, 0) == 1 not " + str(d))
        passed = False;

    if passed:
        print ("Passed all test!");

if __name__ == "__main__":
    tests()
