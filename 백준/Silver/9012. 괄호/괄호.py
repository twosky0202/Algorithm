n = int(input())

for i in range(n):
    data = input()
    stack = []

    for s in data:
        if s =="(":
            stack.append(s)
        elif s == ")":
            if len(stack) == 0:
                stack.append(")")
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print("NO")
    else:
        print("YES")