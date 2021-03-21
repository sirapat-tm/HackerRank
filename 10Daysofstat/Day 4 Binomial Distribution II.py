# Enter your code here. Read input from STDIN. Print output to STDOUT

percent,n = list(map(float, input().rstrip().split()))
p = percent/100

import math
def comb(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def binomial(p,n,start,stop):
    prob = 0
    for i in range(start,stop+1):
        prob = prob+comb(n,i)*p**(i)*(1-p)**(n-i)
    
    return round(prob,3)

print(binomial(p,n,0,2))
print(binomial(p,n,2,10))