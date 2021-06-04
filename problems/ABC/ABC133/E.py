from collections import deque
class Cmb:
    def __init__(self, N, mod=10**9+7):
        self.fact = [1,1]
        self.fact_inv = [1,1]
        self.inv = [0,1]
        
        """ 階乗を保存する配列を作成 """
        for i in range(2, N+1):
            self.fact.append((self.fact[-1]*i) % mod)
            self.inv.append((-self.inv[mod%i] * (mod//i))%mod)
            self.fact_inv.append((self.fact_inv[-1]*self.inv[i])%mod)
    
    """ 関数として使えるように、callで定義 """
    def __call__(self, n, r, mod=10**9+7):
        if (r<0) or (n<r):
            return 0
        return self.fact[n] * self.fact_inv[n-r] % mod

n,k = map(int, input().split())
v = [[] for _ in range(n)]
mod = 10**9+7
for _ in range(n-1):
    a,b = map(int, input().split())
    v[a-1].append(b-1)
    v[b-1].append(a-1)
num_child = [0]*n
root = -1
for i in range(n):
    if len(v[i]) == 1:
        root = i
        break
que = deque([])
for cld in v[root]:
    que.append((root, cld))
while que:
    par, cld = que.pop()
    num_child[par] += 1
    for nx in v[cld]:
        if nx!=par:
            que.append((cld, nx))
c = Cmb(N=k)
ans = k
for e,cld in enumerate(num_child):
    if e==root:
        cand = k-1
    else:
        cand = k-2
    if cld==0:
        continue
    else:
        ans = ans * (c(cand, cld)%mod)
print(ans%mod)