my_list = list(range(50))
my_list.pop(0)
for i in my_list:
    if i == 13:
        continue
    elif i == 40:
        break
    else:
        print(i)