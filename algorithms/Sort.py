#Testing the implementation of a variety of sort functions on arrays of integers

def Bubble(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for num  in range(passnum):
            if alist[num] > alist[num + 1]:
                alist[num], alist[num + 1] = alist[num+1], alist[num]
                print alist

def Selection(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]
        print alist

def Insertion(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue
        print alist

def Merge(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        Merge(lefthalf)
        Merge(righthalf)
        
        i,j,k = 0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1

        print alist

def Quick(i):
    pass

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    Merge(alist)

main()
