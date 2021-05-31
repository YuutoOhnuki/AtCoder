from collections import Counter
n,m = map(int, input().split())
a = list(map(int, input().split()))
cnt = Counter(a)
for _ in range(m):
    b,c = map(int, input().split())
    if c not in cnt.keys():
        cnt[c] = b
    else:
        cnt[c] += b
cnt = sorted(cnt.items(), key=lambda x:x[0], reverse=True)
ans = 0
k = 0
for (x,y) in cnt:
    if k+y <= n:
        ans += x*y
        k += y
    else:
        ans += x*(n-k)
        break
print(ans)