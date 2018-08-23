t = int(input())
answers = []

for _ in range(t):
    bw = list(map(int, input().split()))
    bcwcz = list(map(int, input().split()))
    b = bw[0]
    w = bw[1]
    bc = bcwcz[0]
    wc = bcwcz[1]
    z = bcwcz[2]
    totalCost = 0

    if bc > wc + z:
        bc = wc + z
    if wc > bc + z:
        wc = bc + z
    totalCost = b * bc + w * wc
    answers.append(totalCost)

for answer in answers:
    print(answer)
