lst = list(map(int, input().split()))
s = sum(lst)
flg = False
for i in range(2**4):
    tmp = []
    for j in range(4):
        if (i>>j)&1:
            tmp.append(lst[j])
    if sum(tmp)*2 == s:
        flg = True
print('Yes' if flg else 'No')