import sys
input = sys.stdin.readline

N = int(input())
switch = [0] + list(map(int,input().strip().split()))
M = int(input())
for m in range(M):
    s,n = map(int,input().strip().split())
    if s == 1:
        for i in range(N+1):
            if i % n == 0:
                switch[i] = (switch[i]-1)**2
    elif s == 2:
        w = min(n,N-n+1)
        for i in range(w):
            if i == 0:
                switch[n] = (switch[n]-1)**2
            elif switch[n-i] == switch[n+i]:
                switch[n-i] = (switch[n-i]-1)**2
                switch[n+i] = (switch[n+i]-1)**2
            else:
                break

count = 0
for i in switch[1:]:
     count += 1
     print(i, end = " ")
     if count % 20 == 0:
         print()
        
