n = int(input())
num = 1

for i in range(n):
    num += 6 * i

    if n <= num:
        print(i+1)
        break