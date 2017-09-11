def divisors(n):
    l = []
    for i in range(1,(n/2)+1):
        if n % i == 0:
            l.append(i)
    return l

def amicable(a,b):
    return sum(divisors(a)) == b and sum(divisors(b)) == a and a != b

if __name__ == "__main__":
    l = []
    for i in range(1,10000):
        if amicable(i,sum(divisors(i))) and not (i in l or sum(divisors(i)) in l):
            l.extend([i,sum(divisors(i))])
    print sum(l)
