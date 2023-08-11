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
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    a=sorted(arr)
    ans=[]
    for i,(a,b) in enumerate(zip(arr,a)):
        if a!=b:
            ans.append(i)
    if len(ans)==0:
        print('yes')
    elif len(ans)==2:
        print('yes')
        print('swap'+' '+str(ans[0]+1)+' '+str(ans[1]+1))
    elif len(ans)>2:
        for j in range(1,len(ans)):
            if arr[ans[j-1]]<arr[ans[j]]:
                print('no')
                return
        print('yes')
        print('reverse'+' '+str(ans[0]+1)+' '+str(ans[-1]+1))
        return
    else:
        print('no')
        return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

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
