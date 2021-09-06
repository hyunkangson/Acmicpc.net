from itertools import combinations
import sys,copy

problem = list(sys.stdin.readline().rstrip())
p = []
idx = []

for i,j in enumerate(problem):
    if j == '(':
        problem[i] = ""
        p += [i]
    if j == ')':
        problem[i] = ""
        idx += [[p.pop(),i]]

ans = set()
for i in range(len(idx)):
    for j in combinations(idx,i):
        tmp = copy.deepcopy(problem)
        for k,l in j:
            tmp[k] = "("
            tmp[l] = ")"
        ans.add("".join(tmp))


for i in sorted(ans):
    print(i)