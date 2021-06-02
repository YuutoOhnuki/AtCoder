n,x = map(int, input().split())
l = [0] + list(map(int, input().split()))
pos = 0
ans = 0
for i in range(n+1):
    pos += l[i]
    if pos <= x:
        ans += 1
print(ans)