n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [x for x in a]
for i in range(n):
    if b[i] >= c[i]:
        b[i] -= c[i]
        c[i] = 0
        if b[i] >= 0:
            c[i+1] = max(0, c[i+1]-b[i])
    else:
        c[i] -= b[i]
ans = 0
for i in range(n+1):
    ans += a[i] - c[i]
print(ans)