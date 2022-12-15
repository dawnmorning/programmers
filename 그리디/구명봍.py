def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    # 인덱스 값이 pop한 people의 길이와 같아지면 모두 구출된 것
    while answer < len(people):
        temp = people[answer]
        # 최대 무게 + 최소 무게 =  제한 무게 전까지
        while temp + people[-1] <= limit:
            # 제한에 꽉꽉 눌러 담기
            temp += people.pop()
        answer += 1
    return answer

print(solution([70,50,80,50], 100))