import sys
input = sys.stdin.readline

T = int(input())
white = [[0]*100 for i in range(100)]

for i in range(T):
    x,y = map(int,input().strip().split())
    for j in range(10):
        for k in range(10):
            white[x+j-1][y+k-1] = 1

ans = 0
for i in range(100):
    ans += sum(white[i])
print(ans)

