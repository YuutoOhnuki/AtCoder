n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key=lambda x:x[1])
time = 0
flg = True
for a,b in lst:
    time += a
    if time > b:
        flg = False
        break
print('Yes' if flg else 'No')