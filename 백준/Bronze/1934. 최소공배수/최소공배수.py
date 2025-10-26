t = int(input())

def gcd(a, b):
    while(b > 0):
        a, b = b, a % b
    return a

for i in range(t):
    a, b = map(int, input().split(" "))
    result = (a * b) // gcd(a, b)
    print(result)