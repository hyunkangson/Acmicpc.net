from collections import defaultdict

def solution(s):
    s = s[2:-2].split("},{")
    s.sort(key=len)

    ans = []
    dic = defaultdict(int)
    for i in range(len(s)):
        tmp = list(map(int,s[i].split(",")))
        for j in range(len(tmp)):
            if not dic[tmp[j]]:
                ans.append(tmp[j])
                dic[tmp[j]] = True

    return ans


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))