def solution(routes):
    position = -30001
    routes.sort(key = lambda x: x[1])
    answer = 0

    for route in routes:
        if position < route[0]:
            answer += 1
            position = route[1]
    return answer
