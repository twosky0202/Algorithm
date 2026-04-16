n, m = map(int, input().split())
chess = []
count = []

for i in range(n):
    chess.append(input())

for a in range(n-7):
    for b in range(m-7):
        white_index = 0 # 'W'로 시작
        black_index = 0 # 'B'로 시작
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        white_index += 1
                    if chess[i][j] != 'B':
                        black_index += 1
                else:
                    if chess[i][j] != 'B':
                        white_index += 1
                    if chess[i][j] != 'W':
                        black_index += 1
        count.append(min(white_index, black_index))

print(min(count))