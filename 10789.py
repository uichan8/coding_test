import sys
input = sys.stdin.readline

user = []
for i in range(5):
    user.append(input().strip())

for i in range(15):
    for j in range(5):
        if len(user[j]) > i:
            print(user[j][i],end='')

