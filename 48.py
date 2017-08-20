if __name__ == "__main__":
    c = 0
    for n in range(1,1001):
        c += n**n
    print str(c)[-10:]
