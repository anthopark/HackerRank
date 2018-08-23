squareIntList = []
results = []
n = 1
while n * n <= 1000000000:
    squareIntList.append(n*n)
    n += 1


for _ in range(int(input())):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    
    count = 0
    for num in squareIntList:
        if num >= a and num <= b:
            count += 1
        elif num > b:
            break
    
    results.append(count)

for item in results:
    print(item)