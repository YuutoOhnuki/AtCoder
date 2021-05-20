import string

""" 大文字・小文字の一覧 """
lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
full_chars = string.ascii_letters
digits = string.digits

""" 文字　→　idxへ """
def to_idx(c):
    return ord(c) - ord('a')

""" idx →　文字へ"""
def to_char(idx):
    return chr(idx + ord('a'))


""" 文字列からindexの獲得 """
def get_index(s):
    set_s = set(s)
    dct = {}
    for char in set_s:
        dct[char] = []
    for idx, char in enumerate(s):
        dct[char] += [idx]
    return dct

""" indexの文字を変更 """
def replace_from_idx(s, l_idx, c):
    return s[:l_idx]+c+s[l_idx+len(c):]