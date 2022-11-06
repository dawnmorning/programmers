# import heapq
# def dijkstra(start, n):
#     dist = [float('inf')]*(n+1)
#     dist[start] = 0
#     queue = []
#     heapq.heappush(queue, (0, start))
#     while queue:
#         cost, temp = heapq.heappop(queue)
#         if dist[temp] < cost: continue
#         for i in range(1, n+1):
#             if dist[i] > graph[temp][i] + cost:
#                 dist[i] = graph[temp][i] + cost
#                 heapq.heappush(queue, (dist[i], i))
#     return dist
#
# graph = [[float('inf')]*(201) for _ in range(201)]
# def solution(n, s, a, b, fares):
#     answer = float('inf')
#     for x, y, c in fares:
#         graph[x][y] = c
#         graph[y][x] = c
#     distance = dijkstra(s, n)
#     for i in range(1, n+1):
#         temp = dijkstra(i, n)
#         answer = min(temp[a]+temp[b]+distance[i], answer)
#     return answer
import heapq


def solution(n, s, a, b, fares):
    infinity = 9876543210

    def dijkstra(start, end):
        dist = [infinity] * (n + 1)
        dist[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            cost, idx = heapq.heappop(q)
            if dist[idx] < cost:
                continue
            for i in range(1, n + 1):
                if dist[i] > arr[idx][i] + cost:
                    dist[i] = arr[idx][i] + cost
                    heapq.heappush(q, (dist[i], i))
        return dist

    answer = infinity
    arr = [[infinity] * (n + 1) for _ in range(n + 1)]
    for x, y, cost in fares:
        arr[x][y] = cost
        arr[y][x] = cost
    distance = dijkstra(s, n)
    for i in range(1, n + 1):
        andso_on = dijkstra(i, n)
        answer = min(andso_on[a] + andso_on[b] + distance[i], answer)

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))