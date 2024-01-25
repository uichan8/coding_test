import sys
input = sys.stdin.readline

N = int(input())
for n in range(N):
    count = 0
    D = list(map(int,input().strip().split()))
    for i in range(20):
        for j in range(i):
            count +=  (D[j+1] > D[i+1])
    print(f"{D[0]} {count}")