def primes_sieve(limit):
    prime_dict=dict((i,True) for i in range(2,limit+1))
    print(prime_dict)
    for i in range(2, limit+1):
        if prime_dict[i]:
            yield i
            for n in range(i**2, limit+1, i): 
                prime_dict[n] = False

g=[i for i in primes_sieve(10000)]
print(g)