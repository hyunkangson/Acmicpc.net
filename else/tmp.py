from itertools import permutations

def solution(word):
    vowel = ["A","E","I","O","U"]*5
    dic = []

    for i in range(1,6):
        for j in list(permutations(vowel,i)):
            dic.append("".join(j))

    dic = sorted(list(set(dic)))

    return dic.index(word)+1


print(solution("AAAAE"))