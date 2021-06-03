n,k = map(int, input().split())
if n==2:
    if k!=0:
        print(-1)
    else:
        print(1)
        print('1 2')
else:
    mx = (n-1)*(n-2)//2
    if k > mx:
        print(-1)
    else:
        ans = [(1,i) for i in range(2, n+1)]
        res = mx - k
        cnt = 0
        for i in range(2, n+1):
            if res==cnt:
                break
            for j in range(i+1, n+1):
                if res==cnt:
                    break
                ans.append((i,j))
                cnt += 1
        print(len(ans))
        for x,y in ans:
            print('{} {}'.format(x, y))