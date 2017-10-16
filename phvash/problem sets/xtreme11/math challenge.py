import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

def main(a, b, c):
    return pow(a, ncr(b, c)) % (10**9 + 7)

n = int(input())
for i in range(n):
    a, b, c  = input().strip(" ").split(" ")
    print(main(int(a), int(b), int(c)))

# print(ncr(1000000, 500000))