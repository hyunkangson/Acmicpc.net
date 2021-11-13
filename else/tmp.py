import itertools

def solution(n, weak, dist):
    l = len(weak)
    for i in range(l):
        weak.append(weak[i]+n)

    ans = len(dist)+1

    for start in range(l):
        for d in list(itertools.permutations(dist,len(dist))):
            cnt = 1
            pos = weak[start]+d[cnt-1]
            for i in range(start, start+l):
                if pos < weak[i] :
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[i]+d[cnt-1]

            ans = min(cnt,ans)

    if ans > len(dist):
        return -1
    return ans

print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))