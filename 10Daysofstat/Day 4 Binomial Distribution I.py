import math
boy,girl = list(map(float, input().rstrip().split()))
b = boy/(boy+girl)

def comb(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

prob = 0

for i in range(3,7):
    prob = prob+comb(6,i)*b**(i)*(1-b)**(6-i)
    
print("%.3f" %prob)