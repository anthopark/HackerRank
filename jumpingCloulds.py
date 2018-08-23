n = int(input())
clouds = list(map(int, input().split()))

index = 0
count = 0

while index != n-1:
    if (index + 2 <= n-1 and clouds[index+2]) or index+2 > n-1:
        index += 1
    else:
        index += 2
    count += 1

print(count)