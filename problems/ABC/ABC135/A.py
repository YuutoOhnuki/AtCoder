a,b = map(int, input().split())
if a==b:
    print(0)
else:
    k = (a+b)/2
    if k==int(k):
        print(int(k))
    else:
        print('IMPOSSIBLE')