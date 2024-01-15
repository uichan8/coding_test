import sys
input = sys.stdin.readline

N,S,P= map(int,input().strip().split())
if N == 0:
    print(1)
else:
    score_list = list(map(int,input().strip().split()))
    ans = N
    for n in range(N):
        if score_list[n]<=S:
            ans = n+1
            break

    if N >= P and S <= score_list[P-1]:
        ans = -1

    if N < P and score_list[-1] > S:
        ans = N+1

    print(ans)