import sys

txt = sys.stdin.readline().rstrip()
b = list(sys.stdin.readline().rstrip())
stack = []

for t in txt:
    stack.append(t)
    if len(stack) < len(b):
        continue
    if stack[-len(b):] == b:
        del stack[-len(b):]

if stack:
    print("".join(stack))
else:
    print("FRULA")
