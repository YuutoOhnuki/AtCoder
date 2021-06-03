n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(1, n-1):
    tmp = p[i-1:i+2]
    tmp = sorted(tmp)
    if p[i] == tmp[1]:
        ans += 1
print(ans)