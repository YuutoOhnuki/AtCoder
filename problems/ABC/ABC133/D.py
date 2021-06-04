n = int(input())
a = list(map(int, input().split()))
k = sum(a)//2
ans = [0]*n
ans[0] = k - sum(a[1::2])
for i in range(n-1):
    ans[i+1] = a[i] - ans[i]
ans = [x*2 for x in ans]
print(*ans)