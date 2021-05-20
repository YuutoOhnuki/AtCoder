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