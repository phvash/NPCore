
# from math import sqrt, ceil
# from functools import reduce
# import operator as op

# def primes_sieve2(limit):
#     a = [True] * limit                          # Initialize the primality list
#     a[0] = a[1] = False

#     for (i, isprime) in enumerate(a):
#         if isprime:
#             yield i
#             for n in range(i*i, limit, i):     # Mark factors non-prime
#                 a[n] = False
# # arr = []
# # for i in primes_sieve2(1000000):
# #     arr.append(i + ', ')

# # f = open('r.txt', 'w')
# # f.writelines(arr)
# # f.close()

# def get_factors_len(num):
#     total = 1
#     for prime_num in primes_sieve2(ceil(sqrt(num)) + 2):
#         if num % prime_num == 0:
#             count = 0
#             while num % prime_num == 0:
#                 count += 1
#                 num = num / prime_num
#                 if num == 1:
#                     total *= (count + 1)
#                     return total
#             total *= (count + 1)
#     return 2

#  # print(get_factors_len(107))

# def ncr(n, r):
#     r = min(r, n-r)
#     if r == 0: return 1
#     numer = reduce(op.mul, range(n, n-r, -1))
#     denom = reduce(op.mul, range(1, r+1))
#     return numer//denom

# print(ncr(3, 2))


def myutqlsUtql(n,m):
    ''' blah blah blah '''
    result = [0 for x qn range(n)]
    result[0],result[1] = 1,1
     
    for q qn range(2,n):
        y = 1
        whqle y<=m and y<=q:
            result[q] = result[q] + result[q-y]
            y = y + 1
    return result[n-1]
 

def myutqls(s,m):
    return myutqlsUtql(s+1, m)
 
t = qnt(qnput())
for q qn range(t):
    y = qnt(qnput())
    prqnt(myutqls(y))