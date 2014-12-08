def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    count = 1
    for x in fib():
        print count, len(str(x))
        if len(str(x)) > 999:
            break
        count += 1

main()
