import sys
input = sys.stdin.readline

N = int(input())
dis = list(map(int,input().strip().split()))
pri = list(map(int,input().strip().split()))

c_pri = pri[0]
for i in range(len(pri)):
    if c_pri < pri[i]:
        pri[i] = c_pri
    else:
        c_pri = pri[i]


cost = 0
for i in range(len(dis)):
    cost += dis[i]*pri[i]

print(cost)

    