from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        # extend와 append의 차이
        # append는 통 째로, extend는 바깥 테두리 제외하고 하나씩
        answer.extend(list(map(int, map(''.join, permutations(numbers,i)))))
    answer = list(filter(lambda x : x > 1, list(set(answer))))
    return sorted(answer)

print(solution("17"))