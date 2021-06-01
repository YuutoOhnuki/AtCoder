n,m = map(int, input().split())
s = [set(list(map(int, input().split()))[1:]) for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    tmp = []
    for j in range(n):
        if (i>>j)&1:
            tmp.append(j+1)
    tmp = set(tmp)
    flg = True
    for j in range(m):
        if len(tmp&s[j])%2 != p[j]:
            flg = False
    if flg:
        ans += 1
print(ans)