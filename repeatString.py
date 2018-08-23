def repeatString(s: str, n: int)->int:
    aCount = s.count('a')
    numRepeat = n // len(s)
    if n % len(s) != 0:
        extraIndex = n % len(s)
        extraCount = s[:extraIndex].count('a')
        return aCount * numRepeat + extraCount
    else:
        return aCount * numRepeat

s = input()
n = int(input())

print(repeatString(s, n))