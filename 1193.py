import sys

input = sys.stdin.readline
user = int(input())

line_num = 1
while True:
    if (1 + line_num)*line_num/2 + 1 > user:
        break
    line_num += 1

step_num = user - (1 + line_num-1)*(line_num-1)/2
if line_num%2==0:
    print(f"{int(step_num)}/{int(line_num+1-step_num)}")
else:
    print(f"{int(line_num+1-step_num)}/{int(step_num)}")