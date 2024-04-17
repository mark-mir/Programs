a = [i for i in open('17_9748.txt')]

# максимальный элемент, оканчивающийся на 15
maxi_15 = 0
for k in range(len(a)):
    if (a[k][-3] == '1') and (a[k][-2] == '5'):
        maxi_15 = max(maxi_15, int(a[k]))

count = 0
maxi_summ = 0
for j in range(len(a) - 2):
    if (((len(a[j]) == 5) and (len(a[j + 1]) != 5) and (len(a[j + 2]) != 5)) or ((len(a[j]) != 5) and (len(a[j + 1]) == 5) and (len(a[j + 2]) != 5)) or ((len(a[j]) != 5) and (len(a[j + 1]) != 5) and (len(a[j + 2]) == 5))) and ((int(a[j]) + int(a[j + 1]) + int(a[j + 2])) >= maxi_15):
        count += 1
        maxi_summ = max(maxi_summ, int(a[j]) + int(a[j + 1]) + int(a[j + 2]))

print(count)
print(maxi_summ)
