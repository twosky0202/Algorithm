n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = {}
for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m_list:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")