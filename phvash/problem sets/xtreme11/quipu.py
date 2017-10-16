# Case N == D return 1
# Case N is prime and not a factor of D, return 2
# Case N is not prime and  not a factor of D, return length of 
#        list containing factors of N
# Case N
from math import sqrt, ceil

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def get_factors_len(num):
    total = 1
    for prime_num in primes_sieve2(ceil(sqrt(num)) + 2):
        if num % prime_num == 0:
            count = 0
            while num % prime_num == 0:
                count += 1
                num = num / prime_num
                if num == 1:
                    total *= (count + 1)
                    return total
            total *= (count + 1)
    return 2

def solve(N, D):
    ''' 
        returns the length of multiples of D that are factors of N
    '''

    # Case N == D return 1
    if N == D:
        return 1
    elif N % D != 0:
        return 0
    elif N % D == 0:
        sum = 1
        N_DUP = N
        q = N
        while q >= D:
            # print("N: ", N)
            q = N // D
            r = N % D
            if r == 0:
                if N == D:
                    break
                N = q
                sum += 1
                continue
            else:
                # print('sum: ', sum)
                # print('list: ', factors_list)
                # next_multiple = sorted(list(factors_list))[-(sum + 1)]
                next_multiple = get_next_multiple(q, D)
                # print('next_multiple: ', next_multiple)
                N = next_multiple
                continue
        return sum

def get_next_multiple(current_no, D):
    while current_no > D:
        if current_no % D == 0:
            return current_no
        current_no -= 1
    return 0

def main(N, D):
    global factor_length
    factor_length = get_factors_len(N)
    diff = factor_length - solve(N, D)
    return diff

t, lower_bound, upper_bound = [int(i) for i in input().strip(" ").split(" ")]
for x in range(t):
    D = int(input())
    score = 0
    for N in  range(lower_bound, upper_bound+1):
        score += main(N, D)
        print('score: ', score)
    print(score)

# print(main(99, 3))
# print(solve(99, 3))
# print(get_factors_len(1000000))

# print(get_next_multiple(11, 3))
# print(main(6, 3))
# score = 0
# for N in  range(3, 6+1):
#     score += main(N, 3)
#     print('score: ', score)
# print(main(6, 3))
# 1000000000000, 10000000