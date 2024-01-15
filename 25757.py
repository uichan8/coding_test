import sys
input = sys.stdin.readline

N,G= input().strip().split()
user = set()
for i in range(int(N)):
    user.add(input())

if G == 'Y':
    print(len(user))
if G == 'F':
    print(len(user)//2)
if G == 'O':
    print(len(user)//3)