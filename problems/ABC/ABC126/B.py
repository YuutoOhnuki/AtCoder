s = input()
x, y = int(s[:2]), int(s[2:])
if 1<=x<=12:
    if 1<=y<=12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 1<=y<=12:
    print('YYMM')
else:
    print('NA')