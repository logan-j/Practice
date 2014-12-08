#single and doubly linked lists
from Node import Node

class singleLink():
    
    def __init__(self):
        
        self.fnode = self.pos = self.lnode = None
        self.size = self.position = 0
        
    def __iter__(self):
        temp = self.fnode
        while temp != None:
            yield temp
            temp = temp.get_children()
            
    def add(self, data, index = -1):
        if index == 0 or self.size == 0:
            fnode = Node(data, self.fnode)
            self.fnode = fnode
            if self.size == 0:
                self.lnode  = self.fnode
        elif index < 0 or index == self.size - 1:
            self.lnode.set_children(Node(data))
            self.lnode = self.lnode.get_children()
        elif index > self.size - 1:
            print "index out of bounds"
            quit()
        else:
            temp = self.fnode
            i = 0
            while i != index - 1:
                temp = temp.get_children()
                i += 1
            
            temp.set_children(Node(data, temp.get_children()))
        
        if 0 <= index <= self.position: self.position += 1
        self.size += 1

    def get(self, index):
        if index > self.size - 1 or index < 0:
            print "index out of bounds"
            quit()
        else:
            temp = self.fnode
            i = 0
            while i != index:
                temp = temp.get_children()
                i += 1
            return temp
    
    def remove(self, index):
        if index < 0 or index > self.size - 1:
            print "index out of bounds"
            quit()
        if index == 0:
            self.fnode = self.fnode.get_children()

        
        else:
            temp = self.fnode
            i = 0
            while i != index - 1:
                temp = temp.get_children()
                i += 1
            temp.set_children(temp.get_children().get_children())
        if index == self.size - 1:
            self.lnode = get(self.size-2)
        
        self.size -= 1
        

    def next(self):
        if self.pos == None:
            self.position = 0
            self.pos = self.fnode
        out, self.pos = self.pos, self.pos.get_children()
        
        self.position += 1
        return out


class doubleLink(singleLink):
    pass

def main():
    ls = singleLink()
    ls.add(0)
    ls.add(1)
    ls.add(2)
    ls.add(3, 0)
    ls.remove(0)
    ls.remove(1)

    for item in ls:
        print item
main()
