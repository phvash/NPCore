# Case N == D return 1
# Case N is prime and not a factor of D, return 2
# Case N is not prime and  not a factor of D, return length of 
#        list containing factors of N
# Case N


# def factors(n):
#     return set(x for tup in ([i, n//i] 
#                 for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

from math import sqrt

def factors(n):
    myList = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if (i != n/i):
                myList.append(i)
                myList.append(n // i)
            else:
                myList.append(i)
    return sorted(myList)

def solve(N, D):
    ''' 
        returns the length of multiples of D that are factors of N
    '''
    global factors_list

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
                next_multiple = factors_list[-(sum + 1)]
                # print('next_multiple: ', next_multiple)
                N = next_multiple
                continue
        return sum

def main(N, D):
    global factors_list
    factors_list = factors(N)
    diff = len(factors_list) - solve(N, D)
    return diff

t, lower_bound, upper_bound = [int(i) for i in input().strip(" ").split(" ")]
for x in range(t):
    D = int(input())
    score = 0
    for N in  range(lower_bound, upper_bound+1):
        score += main(N, D)
        # print('score: ', score)
    print(score)

# print(main(6, 3))
# score = 0
# for N in  range(3, 6+1):
#     score += main(N, 3)
#     print('score: ', score)
# print(main(6, 3))
# print(factors(2139289728972897))