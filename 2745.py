import sys
input = sys.stdin.readline

def ascii2int(char):
    if ord('A') <= ord(char):
        return ord(char)-ord('A') + 10
    else:
        return int(char)

num,b = input().split()
b = int(b)

ans = 0
for i in range(len(num)):
    ans += ascii2int(num[len(num) - i - 1]) * (b ** i)
print(ans)