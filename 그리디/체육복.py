def solution(n,lost, reserve):
    reserve.sort()
    cnt = 0
    all_student = [1] * (n+1)
    all_student[0] = 0
    _lost = [l for l in lost if l not in reserve]
    for i in _lost:
        all_student[i] = 0
    _reserve = [r for r in reserve if r not in lost]
    for j in _reserve:
        if j == 1:
            all_student[j+1] = 1
        elif all_student[j-1] == 0:
            all_student[j-1] = 1
        elif j+1 <= n and all_student[j+1] == 0:
            all_student[j+1] = 1
    for k in all_student:
        if k == 1:
            cnt += 1
    return cnt


print(solution(5,[2,4],[1,3,5]))