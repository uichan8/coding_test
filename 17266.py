import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
x = list(map(int,input().strip().split()))

ans = 0
ans = max(x[0], N - x[-1])

for i in range(len(x)-1):
    ans = max(ans, (x[i+1] - x[i])//2 + (x[i+1] - x[i])%2)

print(ans)

