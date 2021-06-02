n,m = map(int, input().split())
a = set([int(input()) for _ in range(m)])
mod = 10**9+7
dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    if i+1<=n and i+1 not in a:
        dp[i+1] += dp[i]
        dp[i+1] %= mod
    if i+2<=n and i+2 not in a:
        dp[i+2] += dp[i]
        dp[i+2] %= mod
print(dp[-1]%mod)