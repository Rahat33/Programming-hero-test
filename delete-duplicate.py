enroll_list = ['a', 'p', 'x', 'i', 'h', 't', 'm', 'l', 'l', 'l','a', 'q']
lottery_list = []

for i in enroll_list:
    if i not in lottery_list:
        lottery_list.append(i)
    else:
        continue

print(lottery_list)