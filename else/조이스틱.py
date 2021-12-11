def solution(name):
    answer = 0

    for i in range(len(name)):
        tmp = ord(name[i])
        if tmp > 78: answer += 90 - tmp + 1
        else: answer += tmp - 65

    if name.count('A') == len(name): return 0

    cnt = [0] * 4
    for i in range(len(name)):
        if name[i] != 'A': cnt[0] = i
        if name[0 - i] != 'A': cnt[1] = i

    if name.count('A') == 0: return answer + max(cnt)

    n = [[] for _ in range(2)]
    for i in range(len(name)):
        if name[i] == 'A': n[0].append(i)
        if name[i] != 'A':
            if len(n[0]) > len(n[1]):
                n[1] = n[0]
                n[0] = []
    if n[1] == []: n[1] = n[0]

    cnt[2] = (n[1][0]-1)*2 + (len(name)-n[1][-1] - 1)
    cnt[3] = (len(name)-n[1][-1] -1)*2 + n[1][0]-1
    if n[1][0] == 0: cnt[2] += 2

    answer += min(cnt)
    return answer