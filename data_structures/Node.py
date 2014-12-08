#basic node class

class Node():
    def __init__(self, data = None, children = None, parent = None):
        self.data = data
        self.children = children
        self.parent = parent
        
    def __str__(self):
        return str(self.data)
        
    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_children(self, children):
        self.children = children

    def set_parent(self, parent):
        self.parent = parent

    def add(self, node):
        self.children.append(node)
