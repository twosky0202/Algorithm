s = input()

for i in range(26):
    code = chr(97+i)
    print(s.find(code), end=" ")