h,w = map(int, input().split())
grid = [input() for _ in range(h)]
t1 = [[0]*w for _ in range(h)]
t2 = [[0]*w for _ in range(h)]

# 横方向への累積和
for i in range(h):
    cnt = 1
    for j in range(w):
        if grid[i][j] == '#':
            cnt = 1
        else:
            t1[i][j] = cnt
            cnt += 1
for i in range(h):
    tmp = -1
    for j in reversed(range(w)):
        if grid[i][j] == '#':
            tmp = -1
        else:
            tmp = max(tmp, t1[i][j])
            t1[i][j] = tmp

# 縦方向への累積和
for j in range(w):
    cnt = 1
    for i in range(h):
        if grid[i][j] == '#':
            cnt = 1
        else:
            t2[i][j] = cnt
            cnt += 1
for j in range(w):
    tmp = -1
    for i in reversed(range(h)):
        if grid[i][j] == '#':
            tmp = -1
        else:
            tmp = max(tmp, t2[i][j])
            t2[i][j] = tmp

# 最大値探索
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, t1[i][j]+t2[i][j]-1)
print(ans)