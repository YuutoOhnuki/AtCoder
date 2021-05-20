"""ナップザック問題(重みが小さい場合)  O(nW)"""
def knapsack_1(N, W, w, v):
    #N : 品物数
    #W : 重みの総和
    #lst (wi,vi) : 商品iの重みwi、価値vi
    
    #dp[i+1][j] : i番目までの品物から重さの総和がj以下になるように選んだ場合の価値の総和の最大値
    dp = [[0 for i in range(W+1)] for _ in range(N+1)]
    
    for i in range(N):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i][j - w[i]] + v[i])
    return dp[N][W]


"""ナップザック問題(価値が小さい場合) O(n sigma(V))"""
def knapsack_2(N, W, w, v):
    #dp[i+1][j] : i番目までの品物から価値の総和がjとなるように選んだ場合の重さの総和の最小値
    #             (そのような解が存在しない場合には十分大きな値INFを採用)  
    
    V = sum(v)
    dp = [[float('inf') for i in range(V+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(V+1):
            if j >= v[i]:
                dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])
            else:
                dp[i+1][j] = dp[i][j]
    res = 0
    for j in range(V+1):
        if dp[N][j] <= W:
            res = j
    return res

""" LCS(最長共通部分列) """
def LCS(s,t):
    ret = ''
    ls,lt = len(s), len(t)
    
    # dp[i][j] : s_i, t_iでのLCS
    dp = [[0]*(lt+1) for _ in range(ls+1)]
    for i in range(ls):
        for j in range(lt):
            if s[i]==t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    if dp[ls][lt]==0:
        return ret
    i,j = ls, lt
    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            ret += s[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    return ret[::-1]