p, d, m, s = tuple(map(int, input().split()))

n = 0
moneySpent = 0
while moneySpent <= s:
    price = p - n*d
    if price <= m:
        price = m
    moneySpent += price
    n += 1

print(n-1)
