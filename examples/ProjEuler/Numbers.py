#Toolsets for dealing with numbers, etc.

from math import sqrt, ceil

def primes(n):
    d = 2
    out = {}
    n = int(n)
    while n > 1:
        if n % d == 0:
            if out.has_key(d):
                out[d] = out[d] + 1
            else:
                out[d] = 1
            n /= d
            
        else:
            d += 1
    return out

#returns the number of factors
def factors(n):
    fac = primes(n)
    out = 1
    for key in fac:
        out *= (fac[key] + 1)
    return out

#takes a list of numbers and returns their lcm
def lcm(n):
    out = {}
    for i in n:
        x = primes(i)
        for k in x:
            if out.has_key(k):
                if x[k] > out[k]:
                    out[k] = x[k]
            else:
                out[k] = x[k]
    num = 1
    for i in out:
        num *= i ** out[i]
    return num

def list_primes(n):
    p = [2]
    for i in xrange(2, n + 1):
        if i % 100000 == 0:
            print "checking: %d" % i
        if is_prime(i, p):
            p.append(i)
    
    return p

def get_prime(n):
    p = [2]
    counter = 3
    while len(p) < n:
        if is_prime(counter, p):
            p.append(counter)
        counter += 1
    return p[len(p) - 1]

def is_prime(n, p):
    if max(p) < n:
        for i in p:
            if i <= sqrt(n) + 1:
                if n % i == 0:
                    return False
            else: break
        return True
    else:
        return False

def baseconvert(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n < 0 or base < 1 or base > 36:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n /= base
        if n == 0:
            break

    return s

def main():


main()
