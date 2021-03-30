import math
def cdfnorm(x,mu,sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 1/2))))

mu,sigma = map(float,input().split())
q1 = float(input())
q2 = list(map(float,input().split()))

print(round(cdfnorm(q1,mu,sigma),3))
print(round(cdfnorm(q2[1],mu,sigma)-cdfnorm(q2[0],mu,sigma),3))