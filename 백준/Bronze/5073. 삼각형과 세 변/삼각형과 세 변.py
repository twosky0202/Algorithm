while True:
    n = list(map(int, input().split()))
    if(n[0]==n[1]==n[2]==0):
        break

    def triangle(n):
        max_side = max(n)
        sum_others = sum(n) - max_side
        if max_side < sum_others:
            return 1
        else:
            return 0

    if(triangle(n) == 0):
        print("Invalid")
    elif(n[0]==n[1]==n[2]):
        print("Equilateral")
    elif(n[0]==n[1] or n[1]==n[2] or n[2]==n[0]):
        print("Isosceles")
    else:
        print("Scalene")