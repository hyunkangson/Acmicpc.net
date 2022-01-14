def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        for j in range(n,i,-1):
            tmp = s[i:j]
            print(tmp)
            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))

    return answer

print(solution("abcdcba"))