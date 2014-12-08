def collatz(n):
    out = [n]
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
        out.append(n)
    return out

def main():
    c = []
    for x in xrange(1, 1000000):
        c.append(len(collatz(x)))
    
    big = index = 0
    for item in c:
        
        if item > big:
            big = item
            print index
        index += 1
    print big
        

