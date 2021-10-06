def solution(enter, leave):
    answer = [0] * len(enter) + [0]
    cur = []

    while leave:
        print(leave,cur, answer)
        if leave[0] in cur:
            tmp = leave.pop(0)
            cur.remove(tmp)
            answer[tmp] += len(cur)
            for c in cur:
                answer[c] += 1
        else:
            cur.append(enter.pop(0))

    return answer[1:]


print(solution([1, 4, 2, 3], [2, 1, 3, 4]))