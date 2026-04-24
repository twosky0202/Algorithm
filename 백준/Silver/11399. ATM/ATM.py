n = int(input())
p = list(map(int, input().split()))
p.sort()
sum = 0
for i in range(n+1):
    for j in range(i):
        sum += p[j]

print(sum)