score = []
m = 0
for _ in range(10):
    score.append(int(input()))

for i in score:
    m += i
    if m >= 100:
        if m - 100 > 100 - (m - i):
            m -= i
        break
print(m)