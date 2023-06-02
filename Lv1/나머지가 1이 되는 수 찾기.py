def solution(n):
    answer = []
    temp_answer = n-1
    answer.append(temp_answer)
    for i in range(n-1,1,-1):
        if n % i == 1:
            answer.append(i)
    value = min(answer)
    return value