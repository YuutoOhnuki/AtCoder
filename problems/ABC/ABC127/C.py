import numpy as np
n,m = map(int, input().split())
x = [0] * (10**5+10)
for _ in range(m):
    l,r = map(int, input().split())
    x[l-1] += 1
    x[r] -= 1
x = np.cumsum(x)
ans = 0
for xx in x:
    if xx == m:
        ans += 1
print(ans)