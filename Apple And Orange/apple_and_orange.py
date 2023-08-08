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
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    cntA = 0
    cntO = 0
    for i in range(len(apples)):
        if apples[i]+a<=t and apples[i]+a>=s:
            cntA+=1
            
    for i in range(len(oranges)):
        if oranges[i]+b<=t and oranges[i]+b>=s:
            cntO+=1
            
    print(cntA)
    print(cntO)
    return

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

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
