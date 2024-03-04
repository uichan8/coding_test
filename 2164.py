from queue import Queue
import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    data = Queue()
    for i in range(1, N + 1):
        data.put(i)
    while data.qsize() != 1:
        data.get()
        data.put(data.get())
    print(data.get())

