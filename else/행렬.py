def rotate(y1,y2,x1,x2,graph):
    r = y1
    c = x1
    cnt = 0
    tmp = graph[r+1][c]
    min_val = tmp

    while True:
        tmp2 = graph[r][c]
        graph[r][c] = tmp
        tmp = tmp2

        if tmp < min_val:
            min_val = tmp

        if c == x2 and r == y1:
            cnt = 2
        elif c == x2 and r == y2:
            cnt = 1
        elif c == x1 and r == y2:
            cnt = 3

        if cnt == 0:
            c += 1
        elif cnt == 1:
            c -= 1
        elif cnt == 2:
            r += 1
        else:
            r -= 1

        if r == y1 and c == x1:
            break

    return graph, min_val


def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1

    for y1,x1,y2,x2 in queries:
        graph, min_val = rotate(y1-1,y2-1,x1-1,x2-1,graph)
        answer.append(min_val)

    return answer




print(solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))