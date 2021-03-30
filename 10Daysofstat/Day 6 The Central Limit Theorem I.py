# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cdfnorm(x,mu,sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

maxw = float(input())
n = float(input())
mu = float(input())
sigma = float(input())

mu_sum = mu*n
sigma_sum = sigma*n**0.5

print(round(cdfnorm(maxw,mu_sum,sigma_sum),4))