import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    change = int(input())
    print(change//25,end = ' ')
    change = change%25
    print(change//10,end = ' ')
    change = change%10
    print(change//5,end = ' ')
    print(change%5)
