n,l = map(int, input().split())
x = [l+i for i in range(n)]
ans = float('inf')
diff = float('inf')
s = sum(x)
for i in range(n):
    tmp = s - x[i]
    if abs(tmp - s) <= diff:
        ans = x[i]
        diff = abs(tmp - s)
print(s - ans)