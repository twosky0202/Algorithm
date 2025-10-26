s = list(input())
result = 10
for i in range(len(s) - 1):
    if(s[i] == s[i+1]):
        result += 5
    else:
        result += 10
print(result)