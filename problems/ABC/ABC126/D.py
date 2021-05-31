from collections import deque
n = int(input())
v = [[] for _ in range(n)]
for _ in range(n-1):
    x,y,w = map(int, input().split())
    v[x-1].append((y-1, w))
    v[y-1].append((x-1, w))
ans = [0] * n
visited = [False] * n
que = deque([(0, 0)])
while que:
    node, col = que.popleft()
    if visited[node]:
        continue
    ans[node] = col
    visited[node] = True
    for (nx, w) in v[node]:
        if (col+w)%2==col:
            nx_col = col
        else:
            nx_col = (col + 1)%2
        que.append((nx, nx_col))
print(*ans, sep='\n')