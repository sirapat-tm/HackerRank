#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):
    if len(arr)%2==0:
        return (arr[math.floor(len(arr)/2)-1]+arr[math.floor(len(arr)/2)])/2
    else: return arr[math.floor(len(arr)/2)]

def q1_2_3(arr):
    sortarr = sorted(arr)
    if len(sortarr)%2==0:
        q1 = median(sortarr[0:len(arr)//2]) 
        q2 = median(sortarr)
        q3 = median(sortarr[len(arr)//2:])
    else :
        q1 = median(sortarr[0:len(arr)//2])
        q2 = median(sortarr)
        q3 = median(sortarr[len(arr)//2+1:])
    return [int(q1),int(q2),int(q3)]   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = q1_2_3(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
