def numToWord(n):
    d = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '10': "ten",
    '11': "eleven",
    '12': "twelve",
    '13': "thirteen",
    '14': "fourteen",
    '15': "fifteen",
    '16': "sixteen",
    '17': "seventeen",
    '18': "eighteen",
    '19': "nineteen",
    '20': "twenty",
    '30': "thirty",
    '40': "forty",
    '50': "fifty",
    '60': "sixty",
    '70': "seventy",
    '80': "eighty",
    '90': "ninety",
    }
    if n == 1000:
        return "onethousand"
    elif n < 20 or (n < 100 and n % 10 == 0):
        return d[str(n)]
    elif n > 20 and n < 100:
        return d[str(n/10)+'0'] + d[str(n%10)]
    elif n / 100 >= 1 and n % 100 == 0:
        return d[str(n/100)] + "hundred"
    elif n > 100 and n % 100 != 0:
        return numToWord(n / 100) + "hundredand" + numToWord(n % 100)

if __name__ == "__main__":
    c = 0
    for i in range(1,1001):
        c += len(numToWord(i))
    print c
