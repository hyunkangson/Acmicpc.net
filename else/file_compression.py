def solution(files):
    renamed = []
    cnt = -1
    for f in files:
        re = ""
        tmp = ""
        c = 0
        cnt += 1
        for i in f:
            if i.isdigit():
                tmp += i
                c = 1
            elif not c:
                re += i.upper()
            else:
                break
        renamed.append([re,int(tmp),cnt,f])

    r = sorted(renamed, key=lambda x: (x[0],x[1],x[2]))
    ans = []
    for x in r:
        ans.append(x[3])
    return ans

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))