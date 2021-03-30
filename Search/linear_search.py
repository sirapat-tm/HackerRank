N,M=list(map(int,input().split()))
A = list(map(int,input().split()))

def linear_search(M):
    for index,value in enumerate(A[::-1]):
        if value==M:
            return len(A)-index
    return -1

print(linear_search(M))