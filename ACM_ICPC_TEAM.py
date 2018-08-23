nm = list(map(int, input().split()))

n = nm[0]
m = nm[1]

attendees = []

for _ in range(n):
    attendee = input()
    attendees.append(int('0b' + attendee, 2))

counts = []
for i in range(n-1):
    for j in range(i+1, n):
        counts.append(bin(attendees[i] | attendees[j]).count('1'))

maxCount = max(counts)
print(maxCount)
print(counts.count(maxCount))
