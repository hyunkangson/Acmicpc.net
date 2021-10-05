import sys


stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))

    if len(cmd) > 1:
        stack.append(cmd[1])

    elif cmd == ["empty"]:
        if not stack:
            print(1)
        else:
            print(0)

    elif cmd == ["top"]:
        if not stack:
            print(-1)
        else:
            print(stack[-1])

    elif cmd == ["size"]:
        print(len(stack))

    elif cmd == ["pop"]:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
