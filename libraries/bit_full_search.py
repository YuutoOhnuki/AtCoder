""" BIT全探索を行う """

# targetにおける部分集合の全組み合わせを返す関数
def bit_fullsearch(target):
    n = len(target)
    ret = []
    for i in range(2**n):
        tmp = []
        for j in range(n):
            if (i>>j)&1:
                tmp.append(lst[j])
        ret.append(tmp)
    return ret

#lst = [1,2,3,4]

lst = [[1,2], [2,3], [3,4], [4,5]]
print(bit_fullsearch(lst))