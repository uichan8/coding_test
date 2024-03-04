import sys
input = sys.stdin.readline

N = int(input())
target = input().strip()
target_vector = [0 for _ in range(ord('Z')-ord('A')+1)]
for c in target:
    target_vector[ord(c)-ord('A')] += 1

count = 0
for i in range(N-1):
    user = input().strip()
    user_vector = [0 for _ in range(ord('Z')-ord('A')+1)]

    for c in user:
        user_vector[ord(c)-ord('A')] += 1
    
    distance = 0
    for j in range(ord('Z')-ord('A')+1):
        distance += abs(user_vector[j]-target_vector[j])
    
    if distance < 2:
        count += 1

    if distance == 2 and len(user) == len(target):
        count+=1
print(count)