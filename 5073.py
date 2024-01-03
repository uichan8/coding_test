import sys
input = sys.stdin.readline

while True:
    user = input().strip().split()
    a,b,c = sorted(map(int,user))

    if a == 0 and b == 0 and c == 0:
        break

    if (c >= a + b):
        print("Invalid")
        continue

    if (a==b and b==c):
        print("Equilateral")
        continue

    if (a == b or b == c or c == a):
        print("Isosceles")
        continue

    print("Scalene")