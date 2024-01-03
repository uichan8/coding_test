import sys
input = sys.stdin.readline
user = map(int,input().split())

H,W,N,M = user
ans = (H//(N+1) + bool(H%(N+1)))*((W//(M+1)) + bool(W%(M+1)))
print(ans)