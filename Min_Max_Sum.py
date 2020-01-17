#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr_sorted = sorted(arr)
    min_sum = sum(arr_sorted[:-1])
    max_sum = sum(arr_sorted[1:])
    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
