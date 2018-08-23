def minimumDistance(n: int, a: list):
    minDList = []
    for i in range(n-1):
        minD = 1001
        for j in range(i+1, n):
            if a[i] == a[j]:
                d = abs(j - i)
                if d < minD:
                    minD = d
        if minD != 1001:
            minDList.append(minD)

    if minDList:
        return min(minDList)
    else:
        return -1


n = int(input())
inputList = list(map(int, input().split()))

print(minimumDistance(n, inputList))
