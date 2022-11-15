def solution(n, results):
    answer = 0
    win = [[]  for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for i,j in results:
        win[i].append(j)
        lose[j].append(i)
    for i in range(1,n+1):
        for w in win[i]:
            if lose[i] :
                for l in lose[i]:
                    if l not in lose[w]:
                        lose[w].append(l)
                    if w not in win[l]:
                        win[l].append(w)

    for a,b in zip(win,lose):
        if len(a)+len(b) == n-1:
            answer+=1
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))