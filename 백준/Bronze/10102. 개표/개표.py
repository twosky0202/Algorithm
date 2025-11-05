v = int(input())
who = list(input())
a_cnt = 0
b_cnt = 0

for i in range(v):
    if(who[i] == "A"):
        a_cnt += 1
    elif(who[i] == "B"):
        b_cnt += 1

if a_cnt > b_cnt:
    print("A")
elif a_cnt < b_cnt:
    print("B")
else:
    print("Tie")