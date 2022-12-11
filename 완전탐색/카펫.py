def solution(brown, yellow):
    n = (brown-4) // 2
    for i in range(n):
        width, height = i, n-i
        if width * height == yellow:
            return [height+2, width+2]