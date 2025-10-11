p = list(input())
is_p = True

for i in range(int(len(p) / 2)):
    if(p[i] != p[len(p)-i-1]):
        is_p = False
        break;

if is_p:
    print("1")
else:
    print("0")