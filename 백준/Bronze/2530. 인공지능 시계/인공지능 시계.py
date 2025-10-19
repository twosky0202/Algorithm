a, b, c = map(int, input().split(" "))
d = int(input())

print((((c+d) // 60 + b) // 60 + a) % 24, ((c+d) // 60 + b) % 60, (c+d) % 60, sep=" ")
