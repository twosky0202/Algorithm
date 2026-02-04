n = int(input())
star = "*"
for i in range(n):
    print(star.rjust(n-i) + " *" * i)
