n, x = map(int, input().split())
list = list(map(int, input().split()))

for i in range(n):
    if(x > list[i]):
        print(list[i], end=" ")