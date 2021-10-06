def solution(weights, head2head):
    n = len(weights)
    data = [[0, 0, 0] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if head2head[i][j] == "N":
                continue

            if head2head[i][j] == "L":
                data[i][1] += 1
            else:
                data[i][0] += 1
                if weights[i] < weights[j]:
                    data[i][2] += 1

        if sum(data[i]) == 0:
            data[i] = [0, 0, weights[i], i + 1]
        else:
            data[i] = [data[i][0] / (data[i][0] + data[i][1]), data[i][2], weights[i], i + 1]

    data = sorted(data, key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    return [i[3] for i in data]

print(solution([60,70,60],	["NNN","NNN","NNN"]))