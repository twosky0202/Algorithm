N = int(input())
array = []
for i in range(N):
    [a, b] = list(map(int, input().split()))
    array.append([a, b])

array.sort()

for i in array:
    print(i[0], i[1])