n,k = map(int, input().split())
a = list(map(int, input().split()))
ans, tmp = 0, 0
right = 0
for left in range(n):
    while right < n:
        if tmp < k:
            tmp += a[right]
            right += 1
        else:
            break
    if tmp >= k:
        ans += n - right + 1
    tmp -= a[left]
print(ans)