def solution(new_id):
    # step1,2
    rev = ""
    for i in range(len(new_id)):
        x = new_id[i]
        if x.isdigit() or x == "_" or x == "-" or x == "_" or \
                x.islower() or x == ".":
            rev += x
        elif x.isupper():
            rev += chr(ord(x)+32)

    # step3
    rmv = rev[0]
    for i in range(1,len(rev)):
        if rev[i] == "." and rev[i] == rev[i-1]:
            continue
        else:
            rmv += rev[i]

    # step4
    if len(rmv):
        if rmv[-1] == ".":
            rmv = rmv[:-1]
    if len(rmv):
        if rmv[0] == ".":
            rmv = rmv[1:]

    # step5
    if not len(rmv):
        rmv = "a"

    # step6
    if len(rmv) >= 16:
        rmv = rmv[:15]
    if len(rmv):
        if rmv[-1] == ".":
            rmv = rmv[:-1]

    # step7
    if len(rmv) <= 2:
        rmv += (3 - len(rmv))* rmv[-1]

    return rmv

print(solution(	"=.="))