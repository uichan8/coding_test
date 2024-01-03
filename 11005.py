import sys
input = sys.stdin.readline

def num2ascii(num):
    if num < 10:
        return str(num)
    return chr(num + ord('A') - 10)

num,b = map(int,input().strip().split())
ans = ''
while num != 0:
    ans = num2ascii(num%b) + ans
    num = num//b

print(ans)