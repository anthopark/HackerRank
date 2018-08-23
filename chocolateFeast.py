def howManyChoco(n: int, c: int, m: int)->int:
    choco = n // c
    totalChoco = wrapper = choco
    while wrapper >= m:
        choco = wrapper // m
        wrapper = wrapper % m + choco
        totalChoco += choco
    return totalChoco


answers = []

for _ in range(int(input())):
    n, c, m = map(int, input().split())
    answers.append(howManyChoco(n, c, m))

for ans in answers:
    print(ans)
