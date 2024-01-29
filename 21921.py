import sys
input = sys.stdin.readline

N,X = map(int,input().strip().split())
user = list(map(int,input().strip().split()))

ans = sum(user[0:X])
temp = ans
count = 1
for i in range(N - X):
    temp = temp - user[i] + user[X + i]
    if temp > ans:
        ans = temp
        count = 1
    elif temp == ans:
        count += 1

if ans:
    print(ans)
    print(count)
else:
    print("SAD")