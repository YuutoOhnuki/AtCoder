"""DAGにおけるトポロジカルソート"""
def topological_sort(n,es):
    # n : node数
    # es : edge
    
    from collections import defaultdict, deque
    ins = defaultdict(int)
    outs = defaultdict(list)
    for v1,v2 in es:
        outs[v1].append(v2)
        ins[v2] += 1
    que = deque(v for v in range(n) if ins[v]==0)
    res = []
    par = [0]*(n+1)
    while que:
        v1 = que.popleft()
        res.append(v1)
        for v2 in outs[v1]:
            ins[v2] -= 1
            if ins[v2] == 0:
                que.append(v2)
                par[v2] = v1
    
    # res : nodeのインデックス
    # par : 各ノードに対する親ノード
    return res, par


# n : ノード数
# m : エッジ数
n,m = map(int,input().split())
es = [[int(x) for x in input().split()] for _ in range(m)]
idx, par = topological_sort(n,es)
print(idx)
print(par)

"""
ex : AtCoder : restore the tree
n,m = 3,3
es = [[1,2],[1,3],[2,3]]

        1 　→　 2
        
        ↓　　↙
        
        3

"""