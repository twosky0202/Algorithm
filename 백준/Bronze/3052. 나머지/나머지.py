list = []
check = False
count = 0

for i in range(10):
    a = int(input())
    if a%42 not in list:
        list.append(a % 42)

print(len(list))