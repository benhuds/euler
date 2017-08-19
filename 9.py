def triple():
    for a in range(2,500):
        for b in range(2,500):
            for c in range(2,500):
                if (a**2) + (b**2) == c**2:
                    if a+b+c == 1000:
                        return a*b*c

if __name__ == "__main__":
    print triple()
