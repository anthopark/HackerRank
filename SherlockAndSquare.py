import math

def squareInterger(a:int, b:int) -> int:
    count = 0
    for num in range(a, b+1):
        if num ** 0.5 == math.floor(num**0.5):
            count += 1
    
    return count

q = int(input())
results = []
for _ in range(q):
    ab = list(map(int, input().split()))
    a = ab[0]
    b = ab[1]
    results.append(squareInterger(a, b))

for item in results:
    print(item)