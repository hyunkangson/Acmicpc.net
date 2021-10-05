from collections import defaultdict

def solution(genres, plays):
    freq = defaultdict(int)
    info = defaultdict(list)

    for i in range(len(plays)):
        freq[genres[i]] += plays[i]
        info[genres[i]].append([plays[i],-i])

    freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    ans = []
    for f in freq:
        tmp = sorted(info[f[0]], key=lambda x:(x[0],x[1]), reverse=True)
        for i in range(len(tmp)):
            if i == 2:
                break
            ans.append(-tmp[i][1])

    return ans



print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))

