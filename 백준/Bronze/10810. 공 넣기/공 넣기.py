n, m = map(int, input().split())
list = [0] * n
for index1 in range(m):
    i, j, k = map(int, input().split())
    for index2 in range(i, j+1):
        list[index2-1] = k
for i in range(n):
    print(list[i], end=" ")