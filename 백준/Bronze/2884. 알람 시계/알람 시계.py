x, y = map(int, input().split())

if(y < 45):
    if(x == 0):
        print(23, 60 - (45 - y))
    else:
        print((x - 1),  60 - (45 - y))
else:
    print(x, y - 45)