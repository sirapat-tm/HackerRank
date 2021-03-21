#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
    if len(arr)%2==0:
        return (arr[math.floor(len(arr)/2)-1]+arr[math.floor(len(arr)/2)])/2
    else: return arr[math.floor(len(arr)/2)]

    # Print your answer to 1 decimal place within this function

def interQuartile(values,freqs):
    
    arr = []
    for i in range(n):
        arr = arr+([values[i]]*freqs[i])
        
    sortarr = sorted(arr)
    if len(sortarr)%2==0:
        q1 = median(sortarr[0:len(arr)//2]) 
        q3 = median(sortarr[len(arr)//2:])
    else :
        q1 = median(sortarr[0:len(arr)//2])
        q3 = median(sortarr[len(arr)//2+1:])
    return print("%.1f" %(q3-q1))
    
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
