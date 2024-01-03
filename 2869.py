import sys
input = sys.stdin.readline

A,B,V = map(int,input().strip().split())
print(int((V-B)/(A-B)) + bool((V-B)%(A-B)))

# 1 A
# 2 2A - B
# 3 3A - 2B
# n n*A - (n-1)B

# An - Bn + B>V
# (A-B)n + B > V
# int((V-B)/(A-B))+1