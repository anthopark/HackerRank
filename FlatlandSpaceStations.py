import math


def maxDistSpaceStation(n: int, m: int, spaceStations: list)->int:
    if n == m:
        return 0

    maxInterval = 0
    curr = 0
    while curr != n-1:
        for stationIndex in spaceStations:
            interval = math.floor(abs(stationIndex-curr)/2 + 1)
            curr = stationIndex
            if interval > maxInterval:
                maxInterval = interval

        curr = n-1
        lastInterval = math.floor(abs(curr - spaceStations[m-1])/2 + 1)
        if lastInterval > maxInterval:
            maxInterval = lastInterval

    return maxInterval//2 + 1


n, m = map(int, input().split())
spaceStations = list(map(int, input().split()))

sorted(spaceStations)

print(maxDistSpaceStation(n, m, spaceStations))
