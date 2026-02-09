def isPalindrome(n):
    size = len(n)
    for i in range(size//2):
        if n[i] != n[size-i-1]:
            return False
    return True

while True:
    n = input()
    if n == "0":
        break
    if isPalindrome(n):
        print("yes")
    else:
        print("no")
