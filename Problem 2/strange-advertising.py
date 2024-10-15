#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    cumulative_likes = 0
    shared = 5  # initial people who see the ad
    for day in range(n):
        liked = shared // 2  # half of the people like the ad
        cumulative_likes += liked
        shared = liked * 3  # those who liked share it with 3 friends
    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
