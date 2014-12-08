from __future__ import print_function
from numpy import uint64
from numpy import bitwise_and
from numpy import bitwise_xor

class board:
    """
    
    
    """
    

    def __init__(self):
       
        wPawn = uint64(0b11111111 << 48)
        wRook = uint64(0b10000001 << 56)
        wNite = uint64(0b01000010 << 56)
        wBish = uint64(0b00100100 << 56)
        wQuen = uint64(0b00001000 << 56)
        wKing = uint64(0b00010000 << 56)
        
        bPawn = uint64(0b11111111 << 8)
        bRook = uint64(0b10000001)
        bNite = uint64(0b01000010)
        bBish = uint64(0b00100100)
        bQuen = uint64(0b00001000)
        bKing = uint64(0b00010000)

        moves = uint64(0)
        
        self.pieces = [bPawn, bRook, bNite, bBish, bQuen, bKing,
                  wPawn, wRook, wNite, wBish, wQuen, wKing]

        wCheck = False
        bCheck = False
        

    def display(self):
        line = "\n" + ":---"*8 + ":"
        lend = "\n:"
        shifts = 0
        compare = 0b1
        while shifts < 64:
            if shifts % 8 == 0: print(line + lend, end='')
            for i in xrange(0, 12):
                space = "   "
                if self.pieces[i] & uint64(compare) != 0:
                    letter = ['p','r','n','b','q','k','P','R','N','B','Q','K']
                    space = " %s " % letter[i]
                    break
            print(space + ":", end='')
            shifts += 1
            compare = compare << 1

        print(line + "\n")

    def move(self, fr, to):
        for i in xrange(0, 12):
            if self.pieces[i] & to != 0:
                self.pieces[i] = self.pieces[i] ^ to
                break
        
        for i in xrange(0,12):
            if self.pieces[i] & fr != 0:
                self.pieces[i] = self.pieces[i] ^ fr ^ to
                break

        
    def select(self, index):
        row = uint64(0xFF)
        col = uint64(0x0101010101010101)
        rdiag = uint64(0x102040810204080)
        ldiag = uint64(0x8040201008040201)
        
        cat = -1 #cat for category; find piece type
        for i in xrange(0, 12):
            if self.pieces[i] & index != 0:
                cat = i
        
        if cat > 0:
            if cat == 0: #black pawn
                pass

            if cat == 6: #white pawn
                pass

            if cat == 1 or cat == 7: #rook
                r = row
                c = col
                while r & index == 0:
                    r = r << uint64(8)
                while c & index == 0:
                    c = c << uint64(1)
                print(bin(c), bin(r))

            if cat == 2 or cat == 8: #knight
                pass

            if cat == 3 or cat == 9: #bishop
                pass

            if cat == 4 or cat == 10: #queen
                pass

            if cat == 5 or cat == 11: #king
                pass
                
        


def main():
    test = board()
    
    
    test.display()
    test.select(uint64(0x8000000000000000))
main()
        
