from itertools import combinations
import sys,copy

txt = list(sys.stdin.readline().rstrip())
n = []
idx = []

for i,j in enumerate(txt):
    if j == '(':
        txt[i] = ""
        n += [i]
    if j == ')':
        txt[i] = ""
        idx += [[n.pop(),i]]

ans = set()
for i in range(len(idx)):
    for j in combinations(idx,i):
        tmp = copy.deepcopy(txt)
        for k,l in j:
            tmp[k] = "("
            tmp[l] = ")"
        ans.add("".join(tmp))


for i in sorted(ans):
    print(i)