sum = 0
avg = 0
for i in range(5):
    n = int(input())
    if(n<40):
        n = 40
    sum += n

avg = sum / 5
print(int(avg))
