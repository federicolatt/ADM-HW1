#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x = arr[-1]
    for i in range(n-1,0,-1): #reversed for, from penultimate element to the first
        if arr[i-1]<x:
            arr[i] = x
            print(*arr)
            return # as soon as the element is inserted, the function returns
        else: #shift
            arr[i] = arr[i-1]
            print(*arr)
    arr[0] = x # if this line is reached, x is the minimum of the entire array, so place it at index 0
    print(*arr)
     

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
