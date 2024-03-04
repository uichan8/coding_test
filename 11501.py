import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int,input().strip().split()))

    profit = 0
    max = data[-1]
    for i in range(N-2,-1,-1):
        target = data[i]
        if target <= max:
            profit += max - target
        else:
            max = target
    print(profit)
        

    