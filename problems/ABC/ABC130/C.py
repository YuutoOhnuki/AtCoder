w,h,x,y = map(int, input().split())
if w/2==x and h/2==y:
    flg = 1
else:
    flg = 0
print(w*h/2, flg)