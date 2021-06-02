n = int(input())
w = list(map(int, input().split()))
ans = float('inf')
for t in range(n+1):
    s1 = sum(w[:t])
    s2 = sum(w[t:])
    ans = min(ans, abs(s1-s2))
print(ans)