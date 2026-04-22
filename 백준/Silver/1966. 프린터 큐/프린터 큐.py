t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    cnt = 1
    while p:
        if p[0] < max(p):
            p.append(p.pop(0))
        else:
            if m == 0:
                break
            p.pop(0)
            cnt += 1
        m = m - 1 if m > 0 else len(p) - 1

    print(cnt)