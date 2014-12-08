#find the largest product of 4 numbers in a grid of 20x20 integers
#in row/column/diagonal

def product(arr):
    out = 1
    for item in arr:
        out *= item
    return out

def main():
    f = open("input.txt", "r")
    lines = []
    for line in f:
        temp = line.split()
        add = []
        for item in temp:
            add.append(int(item))

        lines.append(add)

    row = temp = big = 0
    products = []
    print len(lines), len(lines[0])
    while row < len(lines):
        col = 0
        while col < len(lines[0]):
            if col + 4 < len(lines[0]):
                temp = product(lines[row][col:col + 4])
                products.append(temp)
                if temp > big:
                    big = temp
                    print "F: (%d, %d)" % (row, col) #forward
            
            if row + 4 < len(lines):
                temp = product([lines[row][col], lines[row + 1][col], lines[row + 2][col],
                                lines[row+3][col]])
                products.append(temp)
                if temp > big:
                    big = temp
                    print "D: (%d, %d)" % (row, col) #down
            
            if (col + 4 < len(lines[0]) and row + 4 < len(lines)):
                temp = product([lines[row][col], lines[row+1][col+1], lines[row+2][col+2],
                                lines[row+3][col+3]])
                products.append(temp)
                if temp > big:
                    big = temp
                    print "L: (%d, %d)" % (row, col) #left diagonal
            
            if 2 < col < len(lines[0]) and row + 4 < len(lines):
                temp = product([lines[row][col], lines[row+1][col-1], lines[row+2][col-2],
                                lines[row+3][col-3]])
                products.append(temp)
                if temp > big:
                    big = temp
                    print "R: (%d, %d)" % (row, col) #right diagonal
            
            col += 1
        row += 1

    print big
    

main()
