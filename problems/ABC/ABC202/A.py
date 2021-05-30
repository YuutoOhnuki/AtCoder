lst = list(map(int, input().split()))
ans = 0
for x in lst:
    ans += 7-x
print(ans)