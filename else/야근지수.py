import heapq

def solution(n, works):
    answer = 0

    if sum(works) < n:
        return answer

    work = [-i for i in works]
    heapq.heapify(work)

    for _ in range(n):
        heapq.heappush(work,heapq.heappop(work)+1)

    for w in work:
        answer += w**2

    return answer