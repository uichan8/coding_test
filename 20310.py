import sys
input = sys.stdin.readline

user = input().strip()

zeros = []
ones = []
for i,c in enumerate(user):
    if c == '0':
        zeros.append(i)
    else:
        ones.append(i)

zeros = zeros[:len(zeros)//2]
ones = ones[len(ones)//2:]

ans = [-1 for _ in range(len(user))]

for i in zeros:
    ans[i] = 0

for i in ones:
    ans[i] = 1

for i in ans:
    if i != -1:
        print(i,end="")
