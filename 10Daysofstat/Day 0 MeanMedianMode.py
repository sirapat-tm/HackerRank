import numpy as np
from scipy import stats

N = int(input())
X= [int(item) for item in input().split()] 

print(np.mean(X))
print(np.median(X))
print(int(stats.mode(X)[0]))