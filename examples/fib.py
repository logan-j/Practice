#fibonacci sequence

#assumes there is no 0th fibonacci number. (1, 1, 2, 3, etc.)

#imported for command line options
import sys


#iterative generator function for fibonacci numbers
def fib_iter():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

#generic recursive function
def fib_rec(n = 0):
    if n == 1 or n == 2:
        yield 1
    else:
        for i in fib_rec(n-1):
            for j in fib_rec(n-2):
                yield i + j


def helper():
    print "This is a help message."
    exit()

options = {"-h" : helper, "-r" : fib_rec, "-i" : fib_iter}

arg = sys.argv

number = -1

for item in sys.argv:
    try:
        if item == "-h":
            options[item]()
        elif options.has_key(item):
            func = options[item]
        else:
            number = int(item)
    except ValueError:
        pass

count = 1
for x in fib_rec(count):
    print x
    count += 1
    if count > 10:
        break
