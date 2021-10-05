def solution(sizes):
    a = []
    b = []
    for s in sizes:
        s.sort()
        a.append(s[0])
        b.append(s[1])
    a.sort()
    b.sort()
    return a[-1]*b[-1]

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))