import sys
from math import log2
input = sys.stdin.readline

class heap:
    def __init__(self,N):
        self.data = [0] * (N+2**(int(log2(N))+2))
        self.l = 0

    def push(self,x):
        self.l += 1
        self.data[self.l] = x
        index = self.l
        while index != 1:
            mom = index//2
            if abs(self.data[mom]) > abs(self.data[index]):
                self.data[index], self.data[mom] = self.data[mom], self.data[index]
            elif abs(self.data[mom]) == abs(self.data[index]) and self.data[mom] >= self.data[index]:
                self.data[index], self.data[mom] = self.data[mom], self.data[index]
            else:
                break
            index = mom

    def pop(self):
        print(self.data[1])
        self.data[1] = self.data[self.l]
        self.data[self.l] = 0
        index = 1
        if self.l:
            self.l -= 1
            
        while self.data[2*index]:
            left = 2*index
            right = 2*index + 1 

            if abs(self.data[left]) < abs(self.data[right]) or self.data[right] == 0 or (abs(self.data[left]) == abs(self.data[right]) and self.data[left] <= self.data[right]):
                if abs(self.data[left]) < abs(self.data[index]) or (abs(self.data[left]) == abs(self.data[index]) and self.data[left] <= self.data[index]):
                    self.data[index], self.data[left] = self.data[left], self.data[index]
                    index = left
                else:
                    break

            else:
                if abs(self.data[right]) < abs(self.data[index]) or (abs(self.data[right]) == abs(self.data[index]) and self.data[right] <= self.data[index]):
                    self.data[index], self.data[right] = self.data[right], self.data[index]
                    index = right
                else:
                    break

    
    def __len__(self):
        return self.l

N = int(input())
h = heap(N)

for _ in range(N):
    user = int(input())
    if user == 0:
        h.pop()
    else:
        h.push(user)
