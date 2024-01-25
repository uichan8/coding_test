import sys
input = sys.stdin.readline

T,N = map(int,input().strip().split())
D = []
target = None
for t in range(T):
    d = list(map(int,input().strip().split()))
    if d[0] == N:
        target = d
    D.append(d)

count = 1
for d in D:
    if target[1] < d[1]:
        count+=1

    if target[1] == d[1] and target[2]  < d[2]:
        count += 1

    if target[1] == d[1] and target[2] == d[2] and target[3]  < d[3]:
        count += 1

print(count)