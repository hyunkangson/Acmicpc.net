def solution(triangle):
    l = len(triangle)
    tri = [[] for _ in range(l)]
    tri[0] = triangle[0]

    for i in range(1, l):
        for j in range(len(triangle[i])):
            tmp = triangle[i][j]
            if j == 0:
                tri[i].append(tmp + tri[i - 1][0])
            elif j == len(triangle[i]) - 1:
                tri[i].append(tmp + tri[i - 1][-1])
            else:
                tri[i].append(max(tmp + tri[i - 1][j - 1], tmp + tri[i - 1][j]))

    return max(tri[l - 1])