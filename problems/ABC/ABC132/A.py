s = input()
x = set(s)
flg = True
if len(x)!=2:
    flg = False
else:
    for c in x:
        if s.count(c)!=2:
            flg = False
print('Yes' if flg else 'No')