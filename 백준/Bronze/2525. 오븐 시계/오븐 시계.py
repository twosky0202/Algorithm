a, b = map(int, input().split())
c = int(input())

time = b + c
if(time >= 60):
    a = a + (time // 60)
    b = time % 60
    if(a > 23):
        print(a - 24, b)
    else:
        print(a, b)
else:
    print(a, time)