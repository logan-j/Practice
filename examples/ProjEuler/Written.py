#converts a number input into the written format

def written(n):
    words = ['and', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
             'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
             'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
             'eighty', 'ninety']

    out = ""

    if n / 1000 > 0:
        out += words[n/1000] + " thousand"
        n = n % 1000
    if n / 100 > 0:
        if len(out) != 0: out += " "
        out += words[n/100] + " hundred"
        n = n % 100
    if len(out) > 0:
        if n != 0: out += " %s " % words[0]
    if n > 19:
        out += words[18 + n/10]
        if n % 10 != 0: out += " %s" % words[n%10]
    else:
        if n > 0: out += words[n]
    return out

#counts total letters used to spell out each written representation
def main():
    total = 0
    for x in xrange(1, 1001):
        temp = written(x).split()
        for word in temp:
            total += len(word)
    print total

main()
