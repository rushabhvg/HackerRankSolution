# /*
# BY RUSHABH GALA
# rushabhvg
# GitHub :
# https://github.com/rushabhvg
# StackOverflow :
# https://stackoverflow.com/users/16571212/rushabhvg
# LinkedIn:
# https://www.linkedin.com/in/rushabhvg/
# */

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    elements = [(value, index) for index, value in enumerate(arr)]
    sorted_elements = sorted(elements)
    index_map = {index: i for i, (_, index) in enumerate(sorted_elements)}
    asc_swaps = calculate_swaps(arr, index_map)
    sorted_elements = sorted(elements, reverse=True)
    index_map = {index: i for i, (_, index) in enumerate(sorted_elements)}
    desc_swaps = calculate_swaps(arr, index_map)
    return min(asc_swaps, desc_swaps)


def calculate_swaps(arr, index_map):
    swaps = 0
    visited = [False] * len(arr)

    for i in range(len(arr)):
        if visited[i] or index_map[i] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = index_map[j]
            cycle_size += 1

        if cycle_size > 0:
            swaps += cycle_size - 1

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# /*
# BY RUSHABH GALA
# rushabhvg
# GitHub :
# https://github.com/rushabhvg
# StackOverflow :
# https://stackoverflow.com/users/16571212/rushabhvg
# LinkedIn:
# https://www.linkedin.com/in/rushabhvg/
# */
