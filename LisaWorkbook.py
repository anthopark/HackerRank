n, k = map(int, input().split())
problems = list(map(int, input().split()))
pages = []

for prob in problems:
    keep_track = 0
    while prob != 0:
        if prob >= k:
            probs = [x + keep_track for x in range(k)]
            pages.append(probs)
            keep_track += k
            prob -= k
        else:
            probs = [x + keep_track for x in range(prob)]
            pages.append(probs)
            keep_track += prob
            prob -= prob

# print([page for page in pages])
count = 0
for i in range(len(pages)):
    if i in pages[i]:
        count += 1
print(count)
