freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

# score using character frequency
def score(l):
    s = 0
    for c in l:
        if c.lower() in freqs:
            s += freqs[c.lower()]
    return s

def chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]

def block(l):
    for i in range(3):
        try:
            yield [el[i] for el in l]
        except:
            yield [el[i] for el in l[:-1]]

# takes bitarrays of equal length
def xor(s,t):
    return [chr(a^b) for a,b in zip(s,t)]

def repeatingKeyXor(s,k):
    times = (len(s)//len(k))+1
    return xor(s,(k*times)[:len(s)])

# for every block: find the most likely key for that block by brute force
# i.e. return the key that has the highest score
def decipher(b):
    for n in range(len(b)):
        yield max([(i,score(xor(blocks[n],[i]*len(blocks[n])))) for i in range(97,123)],key=lambda x:x[1])[0]

if __name__ == "__main__":
    # ingest the ciphertext
    f = map(int,open("p059_cipher.txt","r").read().split(','))

    # split into blocks of 3 since we already know key length
    k = list(chunks(f,3))

    # Now transpose the blocks: make a block that is the first byte of every block,
    # and a block that is the second byte of every block, and so on.
    blocks = list(block(k))

    # Solve each block as if it was single-character XOR:
    # For each block, the single-byte XOR key that produces the best looking
    # histogram is the repeating-key XOR key byte for that block. Put them
    # together and you have the key.
    key = ''.join(map(chr,list(decipher(blocks))))
    plaintext = repeatingKeyXor(f,map(ord,key))

    print "Plaintext:\n",''.join(plaintext)
    print sum(map(ord,plaintext))
