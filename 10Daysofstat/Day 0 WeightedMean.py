N = int(input())
X = [int(item) for item in input().split()] 
W = [int(item) for item in input().split()] 

def weightedMean(X, W):
    # Write your code here
    print(round(sum(X[i]*W[i] for i in range(n))/sum(W)),1)

weightedMean(X, W)