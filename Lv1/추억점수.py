def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    information = {}
    for i in range(len(name)):
        information[name[i]] = yearning[i]
    for i, name in enumerate(photo):
        for n in name:
            if n not in information.keys():
                continue
            answer[i] += information[n]
    return answer