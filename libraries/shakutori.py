""" しゃくとり法 """
# 配列Aで同じ文字を含まない最長区間の長さ
n = int(input())
A = list(map(int,input().split()))
l,r = 0,0
v = [False for _ in range(max(A)+1)]
ans = 0
while r<n:
    if not v[A[r]]:
        v[A[r]] = True
        r += 1
        ans = max(ans, r-l)
    elif r==l:
        r += 1
        l += 1
    else:
        v[A[l]] = False
        l += 1
print(ans)

# 配列aの部分和がk以上になるものの個数 (ABC130-D)
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