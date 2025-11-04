t = int(input())
for i in range(t):
    max = 0
    name = ""
    n = int(input())
    for j in range(n):
        s, l = input().split()
        l = int(l)
        if(l > max):
            max = l
            name = s
    print(name)