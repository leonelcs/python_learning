#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    count = 0
    while i < (len(c)-1):
        if (i+2 < len(c) and c[i+2] != 1 ):
            i = i + 2
        else:
            i = i + 1
        count = count + 1
    return count
        
        



if __name__ == '__main__':

    n = int(input())
    c = list(map(int, input().rstrip().split()))

    print(jumpingOnClouds(c))

    
