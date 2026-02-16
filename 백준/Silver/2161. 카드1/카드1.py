n = int(input())
card = [i+1 for i in range(n)]
result = []
while len(card) != 1:
    result.append(card.pop(0))
    card.append(card.pop(0))

for i in result:
    print(i, end=' ')
print(card[0])