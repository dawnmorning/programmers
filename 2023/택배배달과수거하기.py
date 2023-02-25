def solution(cap, n, deliveries, pickups):
#     최소거리 개 싫어
    # 최대한 멀리가면서 뿌리고 돌아오기
    i = n-1
    j = n-1
#     엣지케이스, 인덱스가 -1이 될 수도 있으므로
    while i >= 0 and deliveries[i] == 0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1
    answer = 0
    while i >= 0 and j >= 0:   
        answer += (max(i,j)+1) * 2
        # 배달하자
        current = cap
#         i가 -1 이면 무한루프
        while i >= 0 and current:
            if deliveries[i] > current:
                deliveries[i] -= current
                current = 0
            else:
                current -= deliveries[i]
                deliveries[i] = 0
                while i >= 0 and deliveries[i] == 0:
                    i -= 1
        # 수거하자
        current = cap
        while j >= 0 and current:
            if pickups[j] > current :
                pickups[j] -= current
                current = 0
            else:
                current -= pickups[j]
                pickups[j] = 0
                while j >= 0 and pickups[j] == 0:
                    j -= 1
    return answer

