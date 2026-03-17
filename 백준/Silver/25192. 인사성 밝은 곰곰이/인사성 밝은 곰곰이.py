n = int(input())
s_set = set()
cnt = 0

for i in range(n):
    s = input()
    if s == "ENTER":
        s_set.clear()
        continue
    if s in s_set:
        continue
    else:
        s_set.add(s)
        cnt += 1

print(cnt)