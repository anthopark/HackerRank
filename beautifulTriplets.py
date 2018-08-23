def beautifulTriplets(sq, d):
    btCount = 0
    for num in sq:
        if sq.count(num+d) != 0 and sq.count(num+2*d) != 0:
            btCount += 1

    return btCount


n, d = tuple(map(int, input().split()))
sq = list(map(int, input().split()))

print(beautifulTriplets(sq, d))
