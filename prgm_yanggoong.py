from itertools import combinations_with_replacement

def solution(n, info):
    global answer
    for i in combinations_with_replacement(range(11), n):
        value = 0
        arrow = [0] * 12
        for j in i:
            arrow[j] += 1
        for k in range(11):
            if arrow[k] > info[k]:
                value += (10 - k)
            elif info[k] != 0:
                value -= (10 - k)
        if value <= 0:
            continue
        arrow[11] = value
        if arrow[::-1] > answer[::-1]:
            answer = arrow[:]
        if answer[0] == -1:
            return [-1]
        else:
            return answer[:-1]
# from itertools import combinations_with_replacement
# for i in combinations_with_replacement(range(11),5):
#     print(i)