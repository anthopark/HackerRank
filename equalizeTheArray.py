n = int(input())
inputList = list(map(int, input().split()))
inputList.sort()
count = 1
maxCount = 0

for index in range(1, n):
    if inputList[index] == inputList[index-1]:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 1

if count > maxCount:
    maxCount = count

print(n-maxCount)
