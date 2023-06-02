def solution(a, b, n):
    answer = 0
    
    recyle = n
    while recyle >= a:
        temp = recyle//a * b
        recyle = recyle - (recyle // a) * a + (recyle // a)
        answer += temp
    return answer

print(solution(2,1,20))