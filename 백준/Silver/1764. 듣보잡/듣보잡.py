import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(n):
    set1.add(input().strip())
    
for _ in range(n):
    set2.add(input().strip())

result = sorted(list(set1 & set2)) # 교집합

print(len(result))

for i in result:
    print(i)