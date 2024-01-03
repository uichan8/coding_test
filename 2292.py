import sys
input = sys.stdin.readline
user = int(input())

# 1 -> (1 + 6) -> (1 + 6 + 12) -> (1 + 6 + 12 + 18)
if user == 1:
    print(1)
else:
    user -= 1
    ans = 1
    while True:
        user-=ans*6
        ans+=1
        if user <= 0:
            print(ans)
            break
