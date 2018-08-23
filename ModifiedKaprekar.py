p = int(input())
q = int(input())
kaprekars = []
for n in range(p, q+1):
    d = len(str(n))
    n_square = n * n
    str_n_sq = str(n_square)
    right = str_n_sq[len(str_n_sq)-d:]
    left = str_n_sq[:len(str_n_sq)-d]
    if len(right) == 0:
        right = '0'
    if len(left) == 0:
        left = '0'
    sumRL = int(right) + int(left)
    if sumRL == n:
        kaprekars.append(n)

if kaprekars:
    for n in kaprekars:
        print(str(n) + " ", end="")
    print()
else:
    print("INVALID RANGE")
