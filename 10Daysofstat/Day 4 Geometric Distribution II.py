# Enter your code here. Read input from STDIN. Print output to STDOUT
p_up,p_down = list(map(int, input().rstrip().split()))
p = p_up/p_down
n = int(input())

def geo(n,p):
    return (1-p)**(n-1)*p

print(round(sum([geo(x,p) for x in range(1,6)]),3))
