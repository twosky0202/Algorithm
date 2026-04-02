n = int(input())
books = {}

for i in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max = max(books.values())
best = []

for k, v in books.items():
    if v == max:
        best.append(k)

best.sort()
print(best[0])