import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    data = list(map(int,input().strip().split()))
    count = {}
    for n in range(N):
        if data[n] in count.keys():
            count[data[n]] += 1
        else:
            count[data[n]] = 1
    
    rank_team = []
    for team in count.keys():
        if count[team] == 6:
            rank_team.append(team)

    score = {}
    count = {}
    _5th = {}
    for i in rank_team:
        score[i] = 0
        count[i] = 1
        _5th[i] = 0

    rank = 1
    for n in range(N):
        if data[n] in rank_team:
            if count[data[n]] == 5:
                _5th[data[n]] = rank

            if count[data[n]] <= 4:
                score[data[n]] += rank
            
            count[data[n]] += 1     
            rank+=1

    min_value = min(score.values())  
    min_keys = [k for k, v in score.items() if v == min_value]

    ans = None
    val = 10000
    for k in min_keys:
        if _5th[k] < val:
            val = _5th[k]
            ans = k

    print(ans)
    

    