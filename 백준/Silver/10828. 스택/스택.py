import sys

input = sys.stdin.readline
n = int(input())

stack = []

for i in range(n):
    s = input()
    if "push" in s:
        stack.append(int(s[5:]))
    elif "pop" in s:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in s:
        print(len(stack))
    elif "empty" in s:
        if not stack:
            print(1)
        else:
            print(0)
    elif "top" in s:
        if not stack:
            print(-1)
        else:
            print(stack[-1])