def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]
    maxX, maxY = max(sizes)[0], max(sizes, key = lambda x : x[1])[1]
    return maxX * maxY
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))