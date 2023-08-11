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
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    arr = set()
    ctr=1
    for i in range(len(s)):
        score = ord(s[i])-96
        ctr = ctr+1 if (i+1 != len(s) and s[i+1] == s[i]) else 1
        arr.add(score*ctr)    
    ans = []
    for x in queries:
        if(x in arr):
            ans.append("Yes")
        else:
            ans.append("No")
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

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
