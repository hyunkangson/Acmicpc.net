from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    for c in course:
        tmp2 = []
        for o in orders:
            tmp = combinations(sorted(o),c)
            tmp2 += tmp

        menus = defaultdict(int)
        for t in tmp2:
            menus["".join(t)] += 1
        if not menus:
            continue

        cnt = max(menus.values())
        if cnt <= 1:
            continue

        for i,j in menus.items():
            if j == cnt:
                answer.append("".join(i))

    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],	[2,3,4]))