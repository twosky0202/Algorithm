n = int(input())
grade = list(map(int, input().split()))
max = max(grade)
for i in range(n):
    grade[i] = grade[i]/max * 100

print(sum(grade)/n)