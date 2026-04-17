n = input()
sum = 0
target = -1

for i in range(len(n)):
    if n[i] == '*':
        target = i
        continue
    sum += int(n[i]) if i % 2 == 0 else int(n[i]) * 3

weight = 1 if target % 2 == 0 else 3
for i in range(10):
    if(sum + i * weight) % 10 == 0:
        print(i)
        break