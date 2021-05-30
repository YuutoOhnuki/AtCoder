n,k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key=lambda x:x[0])
pos = 0
for i in range(n):
    a,b = lst[i]
    if (a - pos) > k:
        print(pos + k)
        break
    else:
        k = k - (a - pos) + b
        pos = a
else:
    print(k + pos)