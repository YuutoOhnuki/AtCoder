from collections import deque
n,m = map(int, input().split())
v = [[] for _ in range(n)]
a = list(map(int, input().split()))
for _ in range(m):
    i,j = map(int, input().split())
    v[i-1].append(j-1)
que = deque([])
for i in range(n):
    que.append((i, [a[i]]))
ans = float('inf') * (-1)
while que:
    pos, l = que.pop()
    if len(v[pos]) == 0:
        if len(l)==1:
            pass
        else:
            ans = max(ans, max(l[1:])-l[0])
    else:
        for nx in v[pos]:
            l.append(a[nx])
            que.append((nx, l))
            l = l[:-1]
print(ans)