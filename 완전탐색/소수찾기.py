# from itertools import permutations
#
# def solution(numbers):
#     answer = []
#     for i in range(1, len(numbers)+1):
#         # extend와 append의 차이
#         # append는 통 째로, extend는 바깥 테두리 제외하고 하나씩
#         answer.extend(list(map(int, map(''.join, permutations(numbers,i)))))
#     answer = list(filter(lambda x : x > 1, list(set(answer))))
#     return sorted(answer)
#
# print(solution("17"))

from itertools import permutations

def prime_num(j):
    if j < 2:
        return False
    for i in range(2,j):
        if j%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    li = []
    for i in range(1, len(numbers)+1):
        li.append(list(set(map(''.join, permutations(numbers, i)))))
    # return li
    # sum(덧셈할 것, 처음에 더할 값)
    # int + 리스트가 안 돼서 리스트끼리 합치면 한 리스트 안에 들어감
    temp= list(set(map(int, set(sum(li,[])))))
    # return temp
    for j in temp:
        if prime_num(j) == True:
            answer+=1
    return answer
print(solution("17"))