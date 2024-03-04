import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split())

book = {}
for i in range(N):
    voca = input().strip()
    if len(voca) >= M:
        if voca in book.keys():
            book[voca] += 1
        else:
            book[voca] = 1

s_book = book.keys()
s_rank = []
for v in s_book:
    s_rank.append(10000-(100*book[v] + len(v)))
ans = sorted(zip(s_rank,s_book),reverse=True)
for i in ans:
    print(i[1])



