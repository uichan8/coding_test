import sys
input = sys.stdin.readline

N = int(input())
n_list = sorted(list(map(int,input().strip().split())))
budget = int(input())

exceed = budget - sum(n_list)

if exceed >= 0:
    print(n_list[-1])
    exit(0)

else:
    N += 1
    n_list = [0] + n_list
    for i in range(N-1):
        budget -= n_list[i]
        N -= 1
        limit = budget // N
        if limit >= n_list[i] and limit < n_list[i + 1]:
            print(limit)
            break
        if N == 1:
            print(budget)