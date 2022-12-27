def solution(n,lost, reserve):
#     n = 5
# lost = [2, 4], reserve = [3, 1]
    reserve.sort()
    cnt = 0
    all_student = [1] * (n+1)
    # 1번부터 셀거니깐 인덱스 0은 0으로 바꾸기
    all_student[0] = 0
    # 여벌있는데 도난당한 경우 하나만 남음, 빌려줄 수 없으니 빼놓고 생각
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