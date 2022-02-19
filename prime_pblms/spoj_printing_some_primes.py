# https://www.spoj.com/problems/TDPRIMES/

def some_primes(limit):
    i=2
    prime_count = 0
    while i<limit:
        if is_prime(i):
            prime_count+=1
            if prime_count%100==1:
                print(i)
        i+=1

def is_prime(n):
    j = 2
    is_prime = True
    while j*j<=n:
        if n%j==0:
            return False
        j+=1
    return is_prime


if __name__ == '__main__':
    some_primes(limit = 10**8)