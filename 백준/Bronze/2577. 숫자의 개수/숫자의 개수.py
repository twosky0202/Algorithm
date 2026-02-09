a = int(input())
b = int(input())
c = int(input())

r = str(a*b*c)
r0, r1, r2, r3, r4, r5, r6, r7, r8, r9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in range(len(r)):
    if r[i] == "0":
        r0 = r0+1
    elif r[i] == "1":
        r1 = r1+1
    elif r[i] == "2":
        r2 = r2+1
    elif r[i] == "3":
        r3 = r3+1
    elif r[i] == "4":
        r4 = r4+1
    elif r[i] == "5":
        r5 = r5+1
    elif r[i] == "6":
        r6 = r6+1
    elif r[i] == "7":
        r7 = r7+1
    elif r[i] == "8":
        r8 = r8+1
    elif r[i] == "9":
        r9 = r9+1

print(r0)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)