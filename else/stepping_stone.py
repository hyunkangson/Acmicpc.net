def solution(distance, rocks, n):
    answer = 0
    st = 0
    ed = distance
    rocks.sort()

    while st <= ed:
        mid = (st+ed)//2
        cnt = 0
        r = 0

        for rock in rocks:
            if rock - r < mid:
                cnt += 1
            else:
                r = rock
            if cnt > n:
                break

        if cnt > n:
            ed = mid - 1
        else:
            answer = mid
            st = mid + 1

    return answer

print(solution( 23, [3, 6, 9, 10, 14, 17], 2))