if __name__ == "__main__":
    l = []
    for i in range(0,1000000):
        if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1]:
            l.append(i)
    print sum(l) 
