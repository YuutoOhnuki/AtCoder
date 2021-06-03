s = input()
flg = True
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        flg = False
print('Good' if flg else 'Bad')