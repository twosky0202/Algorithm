n = int(input())
count1 = 0
count0 = 0
for i in range(n):
    a = int(input())
    if(a == 1):
        count1 += 1
    elif(a == 0):
        count0 += 1
if(count1 > count0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")