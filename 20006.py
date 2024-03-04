import sys
input = sys.stdin.readline

p,m = map(int,input().strip().split())

room = []
for i in range(p):
    l,n = input().strip().split()
    l = int(l)

    flag = 0
    for j in room:
        if abs(j[0][1] - l) <= 10 and len(j)< m:
            j.append((n,l))
            flag = 1
            break

    if flag == 0:
        room.append([(n,l)])

for i in room:
    if len(i) == m:
        print("Started!")
    else:
        print("Waiting!")

    i = sorted(i)
    for j in i:
        print(f"{j[1]} {j[0]}")
"""
10 2
10 z
15 b
20 c
25 d
30 e
17 f
18 g
26 h
24 i
100 j
"""

