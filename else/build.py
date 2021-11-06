import sys

def check(frames):
    for x,y,a in frames:
        if a == 0:
            if y == 0 or [x-1,y,1] in frames or [x,y,1] in frames or [x,y-1,0] in frames:
                continue
            else:
                return False
        else:
            if [x,y-1,0] in frames or [x+1,y-1,0] in frames or ([x-1,y,1] in frames and [x+1,y,1] in frames):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b == 1:
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check(answer):
               answer.append([x,y,a])

    return sorted(answer)

print(solution(5,	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))