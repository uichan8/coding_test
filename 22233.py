import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())

memo = set()
for _ in range(N):
    memo.add(input().strip())

for _ in range(M):
    for w in input().strip().split(","):
        memo.discard(w)
    print(len(memo))
            

