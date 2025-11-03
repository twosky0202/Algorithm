n = int(input())
changyeong = 100
sangdeok = 100

for i in range(n):
    a, b = map(int, input().split(" "))
    if(a>b):
        sangdeok -= a
    elif(a<b):
        changyeong -= b

print(changyeong)
print(sangdeok)