from collections import defaultdict
n = int(input())
lst = [list(input().split()) for _ in range(n)]
dic = defaultdict(list)
for x,y in lst:
    dic[x].append(int(y))
dic = sorted(dic.items(), key=lambda x:x[0])
for x, k in dic:
    sk = sorted(k, reverse=True)
    for y in sk:
        print(lst.index([x, str(y)])+1)