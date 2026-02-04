n = int(input())
answer = 0
def factorial(n):
    while True:
        if(n <= 1):
            return 1
        return n * factorial(n - 1)

answer = factorial(n)
print(answer)