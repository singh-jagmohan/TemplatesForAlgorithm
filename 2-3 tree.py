class Node:
    def __init__(self,data,par=None):
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + ' : '+ str(self.data)
        return 'Root : '+ str(self.data)

    def __lt__(self, node):
        return self.data[0]<node.data[0]

    def _isleaf(self):
        return len(self.child)==0

    def _add(self, new_node):
        for child in new_node.child:
            child.paent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
            for child in self.child:
                child.parent = self
        if len(self.data)>2:
            self._split()
    def _insert(self, new_node):
        if self._isleaf():
            self._add(new_node)
        elif new_node.data[0]>self.data[-1]:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0,len(self.data)):
                if new_node.data[0]<self.data[i]:
                    self.child[i]._insert(new_node)
                    break

    def _split(self):
        left_child = Node(self.data[0],self)
        right_child = Node(self.data[2],self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0],self.child[1]]
            right_child.child = [self.child[2],self.child[3]]
        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]
        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._add(self)
        else:
            left_child.parent = self
            right_child.parent = self




class Tree:
    def __init__(self):
        self.root = None
    def insert(self,item):
        if self.root is None:
            self.root = Node(item)
        else:
            self.root._insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return True
    def find(self, item):
        return self.root._find(item)

