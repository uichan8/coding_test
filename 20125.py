import sys
input = sys.stdin.readline

N = int(input())
text = []

for i in range(N):
    text.append(input())

heart_coor = None
for i in range(N):
    for j in range(N):
        if text[i][j] == '*':
            print(f"{i + 2} {j + 1}")
            heart_coor = (i+1,j)
            break
    if heart_coor is not None:
        break
        
ans = []

count = 0
for i in range(0,heart_coor[1]):
    if text[heart_coor[0]][i] == '*':
        count += 1
ans.append(count)

count = 0
for i in range(heart_coor[1]+1,N):
    if text[heart_coor[0]][i] == '*':
        count += 1
ans.append(count)

count = 0
for i in range(N):
    if text[i][heart_coor[1]] == '*':
        count += 1
ans.append(count-2)

count = 0
for i in range(N):
    if text[i][heart_coor[1]-1] == '*':
        count += 1
ans.append(count-1)

count = 0
for i in range(N):
    if text[i][heart_coor[1]+1] == '*':
        count += 1
ans.append(count-1)

for i in ans:
    print(i,end = ' ')