import sys
input = sys.stdin.readline

N, M = map(int,input().strip().split())

name = [-1]
score = [-1]

for _ in range(N):
    T,S = input().strip().split()
    name.append(T)
    score.append(int(S))
    
for _ in range(M):
    user = int(input())
    
    lower = 0
    upper = len(score)-1

    while True:
        index = (lower + upper)//2

        if user <= score[index]:
            upper = index
        else:
            lower = index

        if (upper - index)<2:
            print(name[upper])
            break

