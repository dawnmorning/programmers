# from itertools import permutations
#
# def solution(answers):
#     student1 = []
#     for i in range(1,len(answers)+1):
#         student1.append(i)
#     student2 =
#     # answer = []
#     return student1
# print(solution([1,2,3,4,5]))
def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]  # combination으로 가능?

    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0] * 4
    for i in range(len(answers)):
        if answers[i] == stu1[i % len(stu1)]:
            count[1] += 1
        if answers[i] == stu2[i % len(stu2)]:
            count[2] += 1
        if answers[i] == stu3[i % len(stu3)]:
            count[3] += 1
    # print(count)
    for idx, value in enumerate(count):
        if max(count) == value:
            answer.append(idx)
    answer.sort()
    return answer