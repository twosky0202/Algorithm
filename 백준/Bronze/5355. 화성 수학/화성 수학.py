import sys

data = sys.stdin.read().splitlines() 
n = int(data[0])
results = []

for i in data[1:]:
    a = i.split()
    result = float(a[0])
    
    for j in a[1:]:
        if(j == "@"):
            result *= 3
        elif(j == "%"):
            result += 5
        elif(j == "#"):
            result -= 7
    results.append(f"{result:.2f}")

print("\n".join(results))        