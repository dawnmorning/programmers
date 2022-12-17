def find_parent(parent, x):
    if parent[x] != x:  # 루트가 아니라면
        parent[x] = find_parent(parent, parent[x])  # 루트 찾으러 계속 올라가기
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def solution(n, costs):
    parent = [x for x in range(n)]
    costs.sort(key=lambda x: x[2])
    answer = 0
    cnt = 0
    for x, y, cost in costs:
        # find 연산 후 부모가 다른지 확인하고 합집합할 것. parent[x] 하면 틀림
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            answer += cost
            cnt += 1
        if cnt == n - 1:
            return answer

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))