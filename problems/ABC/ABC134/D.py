n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(n+1)]
for i in reversed(range(1, n+1)):
    tmp = b[::i]
    if sum(tmp)%2!=a[i-1]:
        b[i] += 1
ans = []
for e,x in enumerate(b):
    if x!=0:
        ans.append(e)
print(len(ans))
if len(ans)!=0:
    print(*ans)