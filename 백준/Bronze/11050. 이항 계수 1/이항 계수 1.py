def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

n, k = map(int, input().split())

print(factorial(n) // (factorial(n-k) * factorial(k)))