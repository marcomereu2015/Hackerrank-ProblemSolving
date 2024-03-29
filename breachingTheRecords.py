#Breaking the Records. ~ Python 3


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_count = min_count = 0
    max = min = scores[0]

    for i in range(1,len(scores)):
        if max < scores[i]:
            max = scores[i]
            max_count += 1
        elif min > scores[i]:
            min = scores[i]
            min_count += 1
    return max_count, min_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
