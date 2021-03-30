n = float(input())
mu = float(input())
sigma = float(input())
dist = float(input())
z = float(input())

sigma_sample = sigma / (n**0.5)

print(round(mu - (sigma_sample*z),2))
print(round(mu + (sigma_sample*z),2))