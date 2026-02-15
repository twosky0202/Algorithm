import sys
input = sys.stdin.readline

n = int(input())
sum = 0
for i in range(n):
    sum = sum + int(input())
    if i != n-1:
        sum = sum - 1
print(sum)