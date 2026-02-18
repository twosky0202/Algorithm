n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = {}
for i in m_list:
    dic[i] = 0

for j in n_list:
    if j in dic:
        dic[j] = 1

for d in dic:
    print(dic[d], end=' ')