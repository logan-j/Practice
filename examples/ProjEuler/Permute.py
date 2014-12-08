def permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList= []
    for i in range(0, len(prevList)):
        for j in range(0, len(string)):
            newString = prevList[i][0:j] + string[0] + prevList[i][j:len(string) -1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

#find the millionth permutation of a set of digits
def ordered(string):
    from math import factorial as fac
    out = []
    temp = times = 0
    for i in xrange(9, 0, -1):
        times = 0
        while True:
            if temp + fac(i) < 1000000:
                times += 1
                temp += fac(i)
                print temp
            else:
                out.append(times)
                break
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for item in out:
        print l.pop(item)

