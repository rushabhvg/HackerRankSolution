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
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    unfair = sys.maxsize
    for i in range(len(arr)-k+1):
        if(arr[i+k-1]-arr[i]<unfair):
            unfair = arr[i+k-1]-arr[i]
            
    return unfair
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

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
