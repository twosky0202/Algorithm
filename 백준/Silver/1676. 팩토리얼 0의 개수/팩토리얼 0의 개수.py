def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input())
cnt = 0

num = str(factorial(n))

for i in range(len(num)):
    if num[-1 - i] != '0':
        break
    cnt += 1

print(cnt)