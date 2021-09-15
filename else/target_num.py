def solution(numbers, target):

    def dfs(idx,n):
        global ans
        if idx == len(numbers):
            if n == target:
                ans += 1
            return

        dfs(idx+1,n+numbers[idx])
        dfs(idx+1,n-numbers[idx])


    global ans
    ans = 0
    dfs(0,0)

    return ans

print(solution([1, 1, 1, 1, 1],	3))