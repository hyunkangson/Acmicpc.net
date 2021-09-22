def solution(n):
    answer = ''
    while n:
        x = 0
        tmp = n%3
        if not tmp:
            x = 1
            tmp = 4

        if n < 3:
            answer += str(tmp)
            break

        n //= 3
        n -= x
        answer += str(tmp)

    return answer[::-1]

for i in range(1,12):
    print(solution(i))