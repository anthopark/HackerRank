def librayFine(dmy1, dmy2):
    d1 = dmy1[0]
    m1 = dmy1[1]
    y1 = dmy1[2]

    d2 = dmy2[0]
    m2 = dmy2[1]
    y2 = dmy2[2]

    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500*(m1 - m2)
        elif m1 == m2:
            if d1 > d2:
                return 15*(d1 - d2)
            else:
                return 0
        else:
            return 0
    else:
        return 0



dmy1 = list(map(int, input().split()))
dmy2 = list(map(int, input().split()))

print(librayFine(dmy1, dmy2))