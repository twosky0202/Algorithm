n, m = map(int, input().split())
list = []
for i in range(n):
    list.append(i+1)

for index in range(m):
    i, j = map(int, input().split())
    k = list[i-1:j]
    k.reverse()
    list[i-1:j] = k

for i in range(n):
    print(list[i], end=" ")