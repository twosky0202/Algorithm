import sys

n = int(input())
arr = []

for _ in range(n):
    i = int(sys.stdin.readline())
    arr.append(i)

sorted_arr = sorted(arr)

for i in range(n):
    print(sorted_arr[i])