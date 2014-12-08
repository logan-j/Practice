#palindromes

def isPalindrome(n):
    temp = str(n)
    rev = temp[::-1]
    return temp == rev

def main():
    num = []
    for i in xrange(700, 999):
        for j in xrange(700, 999):
            if isPalindrome(i * j):
                num.append(i*j)
    print max(num)

main()
