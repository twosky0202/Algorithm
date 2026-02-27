N = int(input())
A = set(map(int, input().split()))
M = int(input())
l = list(map(int, input().split()))

for num in l:
    if num in A:
        print(1)
    else:
        print(0)