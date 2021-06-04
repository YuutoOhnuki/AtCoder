l,r = map(int, input().split())
if r-l >= 2018:
    print(0)
else:
    ans = float('inf')
    mod = 2019
    mx = min(r, l+2019)
    for i in range(l, mx+1):
        for j in range(i+1, mx+1):
            ans = min(ans, i*j%mod)
    print(ans)