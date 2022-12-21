def solution(number, k):
    # 정렬해서 큰 수를 찾는 것이 아니라, 차례대로 들어오는데, 그 안에서 최대 숫자 만드는 것
    answer = ''
    temp = []
    # 숫자들 들어올 때 마다 먼저 있는 수보다 크다면, 앞의 수는 지우고 k(횟수) 차감
    for i in number:
        while temp and temp[-1] < i and k > 0:
            k -= 1
            temp.pop()
        temp.append(i)
    # 있는 숫자들 합치기
    answer = ''.join(temp[:len(temp) - k])
    # print('목요일 수정중')
    return answer