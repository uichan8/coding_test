import sys
input = sys.stdin.readline

while True:
    target = input().strip()
    if target == "end":
        break

    flag = 0
    for i in range(len(target)-1):
        if target[i] == target[i+1] and target[i:i+2] != 'ee' and target[i:i+2] != 'oo': 
            flag = 1

    state = []
    for c in target:
        if c in ['a','e','i','o','u']:
            state.append(1)
        else:
            state.append(0)

    for i in range(len(target)-2):
        if state[i] == state[i+1] and state[i + 1] == state[i+2]:
            flag = 1
    if sum(state) == 0:
        flag = 1

    if flag:
        print(f"<{target}> is not acceptable.")
    else:
        print(f"<{target}> is acceptable.")