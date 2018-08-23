def cutTheStick(input_list: list)->list:
    answers = []
    answers.append(len(input_list))
    count = 0
    while len(input_list) > 0:
        shortest = min(input_list)
        count = input_list.count(shortest)
        if len(input_list) - count == 0:
            break
        answers.append(len(input_list) - count)
        for _ in range(count):
            input_list.remove(shortest)
    
    return answers


n = int(input())
input_list = list(map(int, input().split()))

answers = cutTheStick(input_list)
for num in answers:
    print(num)