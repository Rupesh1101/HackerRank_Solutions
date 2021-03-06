#!/bin/python3
import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    lst = [0] * (n + 2)
    for a, b, k in queries:
        lst[a] += k
        lst[b + 1] -= k

    max_ = temp = 0
    for val in lst:
        temp += val
        max_ = max(max_, temp)
    return max_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
