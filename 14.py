def collatzAux(n,c):
    if n == 1:
        return c
    elif n%2 == 0:
        return collatzAux(n/2,c+1)
    else:
        return collatzAux((3*n)+1,c+1)

def collatz(n):
    return collatzAux(n,1)

if __name__ == "__main__":
    #print collatz(13)
    n = (0,0)
    for i in range(2,1000000):
        if collatz(i) > n[1]:
            n = (i,collatz(i))
    print n
