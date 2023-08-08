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
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    cnt = 0
    for i in range (0, len(s)-2, 3):
        if(s[i]!="S"):
            cnt += 1
        if(s[i+1]!="O"):
            cnt += 1
        if(s[i+2]!="S"):
            cnt += 1
    
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

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
