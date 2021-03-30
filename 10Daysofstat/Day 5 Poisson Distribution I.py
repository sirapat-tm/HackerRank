# Enter your code here. Read input from STDIN. Print output to STDOUT
mu = float(input())
k = int(input())

import math
def poiss(k,mu):
    return (mu**k)*math.exp(-mu)/math.factorial(k)

print(round(poiss(k,mu),3))