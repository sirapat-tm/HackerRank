import math
def cdfnorm(x,mu,sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 1/2))))

mu,sigma = map(float,input().split())
q1 = float(input())
q2 = float(input())

print(round((1-cdfnorm(q1,mu,sigma))*100,2))
print(round((1-cdfnorm(q2,mu,sigma))*100,2))
print(round(cdfnorm(q2,mu,sigma)*100,2))