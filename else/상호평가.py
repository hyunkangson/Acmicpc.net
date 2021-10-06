def chk(n):
    print(n)
    if n >= 90:
        return "A"
    elif 80 <= n <90:
        return "B"
    elif 70 <= n <80:
        return "C"
    elif 50<= n<70:
        return "D"
    else:
        return "F"


def solution(scores):
    answer = ''
    s = len(scores)
    data = [[] for _ in range(s)]

    for i in range(s):
        for j in range(s):
            if i == j:
                data[i].append(-scores[j][i])
            else:
                data[i].append(scores[j][i])
        data[i].sort()

    for i in range(s):
        tmp = -data[i].pop(0)
        if tmp < data[i][0] or tmp > data[i][-1]:
            answer += chk(sum(data[i][:])/(s-1))
        else:
            answer += chk((sum(data[i][:])+tmp)/s)

    return answer