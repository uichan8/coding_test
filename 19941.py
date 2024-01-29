import sys
input = sys.stdin.readline

N,K = map(int,input().strip().split())
table_str = input().strip()
table = [i for i in table_str]

count = 0

for i in range(len(table)):
    if table[i] == "P":
        table[i] = "N"

        for j in range(max(0,i - K),min(i + K + 1, N)):
            if table[j] == "H":
                table[j] = "N"
                count += 1
                break


print(count)