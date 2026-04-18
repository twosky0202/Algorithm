l = int(input())
s = input()
mod = 1234567891
hash = 0

for i in range(l):
    num = ord(s[i]) - 96 # 아스키 코드에서 96 빼주기
    hash += num * 31 ** i

print(hash % mod)