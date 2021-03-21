#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(vals):
    # Print your answers to 1 decimal place within this function
    mean = sum(vals)/len(vals)
    std = (sum([(x-mean)**2 for x in vals])/len(vals))**(1/2)
    return print(f"{std:.1f}")

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
