n = int(input())
arr = ""

for i in range(n):
    sum = 0
    cnt = 0
    arr = input()
    for j in arr:
        if j == "O":
            cnt += 1
            sum += cnt
        elif j == "X":
            cnt = 0
    print(sum)