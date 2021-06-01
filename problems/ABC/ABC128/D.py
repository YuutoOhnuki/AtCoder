n,k = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(n+1):
    for j in range(n-i+1):
        tmp = v[:i] + v[n-j:]
        if len(tmp) <= k:
            tmp = sorted(tmp)
            r = k - len(tmp)
            for _ in range(r):
                if tmp:
                    if tmp[0] < 0:
                        tmp = tmp[1:]
            ans = max(ans, sum(tmp))
print(ans)