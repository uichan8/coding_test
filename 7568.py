import sys
input = sys.stdin.readline

N = int(input())

X = []
Y = []
RANK = [1]*N

for n in range(N):
    x,y = map(int,input().strip().split())
    X.append(x)
    Y.append(y)

    for i in range(n):
        if X[i] > x and Y[i] > y:
            RANK[n] += 1
        if X[i] < x and Y[i] < y:
            RANK[i] += 1

for i in RANK:
    print(i,end = ' ')
