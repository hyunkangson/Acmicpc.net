def solution(lottos, win_nums):
    zeros = 0
    wins = 0
    for i in lottos:
        if i == 0:
            zeros += 1
            continue
        if i in win_nums:
            wins += 1

    if wins == 0:
        if zeros == 0:
            return ([6,6])
        return ([7-zeros,6])

    return ([7-(zeros+wins), 7-wins])