n = int(input())
l = list(map(int, input().split()))
t, p = map(int, input().split())

t_bundle = 0
p_bundle = 0

for i in l:
    if i == 0:
        continue
    elif i <= t:
        t_bundle += 1
    elif i % t == 0:
        t_bundle += i // t
    else:
        t_bundle += i // t + 1
print(t_bundle)
print(n // p, n % p)