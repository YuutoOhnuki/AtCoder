n = int(input())
p = list(map(int, input().split()))
flg = False
for i in range(n):
    for j in range(i, n):
        tmp = []
        for k in range(n):
            if k==i:
                tmp.append(p[j])
            elif k==j:
                tmp.append(p[i])
            else:
                tmp.append(p[k])
        tf = True
        for k in range(1, n):
            if tmp[k] <= tmp[k-1]:
                tf = False
        if tf:
            flg = True
print('YES' if flg else 'NO')