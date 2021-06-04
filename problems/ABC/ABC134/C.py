n = int(input())
a = [int(input()) for _ in range(n)]
s = sorted(a)
if s[-1]==s[-2]:
    for i in range(n):
        print(s[-1
        ])
else:
    for i in range(n):
        if a[i]==s[-1]:
            print(s[-2])
        else:
            print(s[-1])