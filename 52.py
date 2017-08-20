def rearrange(n):
    return ''.join(sorted(str(n)))

if __name__ == "__main__":
    for n in range(1,500000):
        if rearrange(n) == rearrange(2*n) == \
            rearrange(3*n) == rearrange(4*n) == \
            rearrange(5*n) == rearrange(6*n):
            print n
            break
