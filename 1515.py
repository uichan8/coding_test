import sys
input = sys.stdin.readline

user = input().strip()

ii = 1
while True:
    i = str(ii)
    while True:
        if len(i) == 0 or len(user) == 0: 
            break
        index = i.find(user[0])
        if index == -1:
            break
        user = user[1:]
        i = i[index+1:]

    if len(user) == 0:
        print(ii)
        break

    ii += 1
    