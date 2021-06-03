import math

def gcd(a,b):
    return math.gcd(a,b)

def lcm(a,b):
    f = gcd(a,b)
    return a*b//f

def f(x, c, d):
    l = lcm(c,d)
    p = x//c
    q = x//d
    r = x//l
    return x + r - p - q

a,b,c,d = map(int, input().split())
print(f(b,c,d) - f(a-1, c,d))