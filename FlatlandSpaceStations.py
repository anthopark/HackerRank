
def maxDistSpaceStation(n: int, m: int, spaceStations: list)->int:
    if n == m:
        return 0
    maxMidSeg = 0
    curr = -1
    for ss in spaceStations:
        seg = ss - curr - 1
        if curr == -1:
            firstSeg = seg
        curr = ss
        maxMidSeg = max(maxMidSeg, seg)
    maxMidDist = (maxMidSeg + 1) // 2

    lastSeg = n - curr - 1

    maxDist = max(firstSeg, maxMidDist, lastSeg)

    return maxDist


n, m = map(int, input().split())
spaceStations = list(map(int, input().split()))

spaceStations.sort()

print(maxDistSpaceStation(n, m, spaceStations))
