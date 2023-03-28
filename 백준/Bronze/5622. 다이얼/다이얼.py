a = input()
sum = 0
for i in range(len(a)):
    if(a[i] >= 'A' and a[i] <= 'C'):
        sum += 2
    elif(a[i] >= 'D' and a[i] <= 'F'):
        sum += 3
    elif(a[i] >= 'G' and a[i] <= 'I'):
        sum += 4
    elif(a[i] >= 'J' and a[i] <= 'L'):
        sum += 5
    elif(a[i] >= 'M' and a[i] <= 'O'):
        sum += 6
    elif(a[i] >= 'P' and a[i] <= 'S'):
        sum += 7
    elif(a[i] >= 'T' and a[i] <= 'V'):
        sum += 8
    elif(a[i] >= 'W' and a[i] <= 'Z'):
        sum += 9

print(sum+int(len(a)))
