from itertools import permutations

def property(l):
    return (int(l[1]+l[2]+l[3]) % 2 == 0 and
    int(l[2]+l[3]+l[4]) % 3 == 0 and
    int(l[3]+l[4]+l[5]) % 5 == 0 and
    int(l[4]+l[5]+l[6]) % 7 == 0 and
    int(l[5]+l[6]+l[7]) % 11 == 0 and
    int(l[6]+l[7]+l[8]) % 13 == 0 and
    int(l[7]+l[8]+l[9]) % 17 == 0)

if __name__ == "__main__":
    l = [str(x) for x in range(0,10)]
    nums = [''.join(n) for n in list(permutations(l))]
    c = []
    for n in nums:
        if property(n):
            c.append(int(n))
    print sum(c)
