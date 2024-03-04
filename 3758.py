import sys
input = sys.stdin.readline

T = int(input()) #테스트 데이터수
for _ in range(T):
    n,k,t,m = map(int,input().strip().split()) # 팀갯수 문제갯수 팀아이디 로그 엔트리갯수

    score = [[0 for _ in range(k)] for _ in range(n)]
    assign = [0 for _ in range(n)]
    last = [0 for _ in range(n)]

    for i in range(m):
        s,l,o = map(int,input().strip().split()) # 팀 id 문제 번호 획득 점수
        last[s-1] = i
        assign[s-1] += 1
        score[s-1][l-1] = max(score[s-1][l-1],o)

    last_score = [sum(i) for i in score]
    
    target_score = last_score[t-1]
    target_assign = assign[t-1]
    target_last = last[t-1]
    rank = 1
    for i in range(n):
        if target_score < last_score[i]:
            rank += 1
        elif target_score == last_score[i] and target_assign > assign[i]:
            rank += 1
        elif target_score == last_score[i] and target_assign == assign[i] and target_last > last[i]:
            rank += 1            

    print(rank)

                          
    
