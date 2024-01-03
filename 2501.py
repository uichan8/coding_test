import sys
input = sys.stdin.readline

a,b = map(int,input().strip().split())

count = 0
for i in range(int(a )):
    if a % (i+1) == 0:
        count+=1
        if count == b:
            print(i+1)
            break

if count<b:
    print(0)