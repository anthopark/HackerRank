def serviceLane(widths: list, cases: list)->list:
    answers = []
    for case in cases:
        answers.append(min(widths[case[0]:case[1]+1]))
    return answers


n, t = map(int, input().split())
widths = list(map(int, input().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().split())))
answers = serviceLane(widths, cases)

for ans in answers:
    print(ans)
