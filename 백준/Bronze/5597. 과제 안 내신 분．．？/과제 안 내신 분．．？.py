list = [0] * 30
for i in range(28):
    a = int(input())
    list[a-1] = a

for i in range(30):
    if(list[i] == 0):
        print(i+1)