n = int(input())
sugar = 0

while n > 0:
    if n % 5 == 0:
        sugar += n // 5
        n = 0
    else:
        n -= 3
        sugar += 1

if n == 0:
    print(sugar)
else:
    print(-1)