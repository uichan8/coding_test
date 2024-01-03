import sys
input = sys.stdin.readline

times = int(input())
ans = [0]*21
for i in range(times):
    user = input().strip().split()
    if len(user) == 2:
        inst, val = user
        val = int(val)
    else:
        inst = user[0]

    if inst == 'all':
        ans = [1]*21

    elif inst == 'empty':
        ans = [0]*21
    
    elif inst == 'add':
        ans[val] = 1

    elif inst == 'remove':
        ans[val] = 0

    elif inst == 'check':
        print(ans[val])

    elif inst == 'toggle':
        ans[val] = (ans[val]-1)**2




