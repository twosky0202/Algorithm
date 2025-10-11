A = 300
B = 60
C = 10
a = 0
b = 0
c = 0

n = int(input())
if(n % 10 != 0):
    print("-1")
else:
    a = int(n / A)
    b = int(n % A / B)
    c = int(n % A % B / C)
    print(str(a)+" "+str(b)+" "+str(c))
