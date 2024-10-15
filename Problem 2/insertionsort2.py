#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    for i in range(1, n):
        x = arr[i]
        for j in range(i, 0, -1):
            if arr[j-1] < x:
                arr[j] = x
                break
            else:
                arr[j] = arr[j-1]
        else: #if the whole for loop, ends without a break
            arr[0] = x
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
