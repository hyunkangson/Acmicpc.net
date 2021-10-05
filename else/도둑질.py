def solution(money):
    l = len(money)
    dp = [money[0]] + [0]*(l-1)
    dp2 = [0] + [0]*(l-1)

    for i in range(1,l):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(dp[-2],dp2[-1])

print(solution([1, 2, 3, 1]))