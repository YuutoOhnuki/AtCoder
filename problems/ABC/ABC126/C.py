n,k = map(int, input().split())
ans = 0
for i in range(1, n+1):
    cnt = 0
    while i < k:
        cnt += 1
        i *= 2
    ans += (1/n) * ((1/2)**cnt)
print(ans)