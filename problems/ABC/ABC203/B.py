n,k = map(int, input().split())
x = (1+k)*k//2
ans = 0
for i in range(1, n+1):
    ans += x
    ans += (i*100)*k
print(ans)