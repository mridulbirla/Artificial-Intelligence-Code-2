__author__ = 'mridul'


class Node:

    def __init__(self,identifier,parent=None):

        self.val=identifier
        self.children = []
        self.eligible_swap = []
        self.parent=parent
        self.priority=10000

    def add_children(self,child):

        self.children.append(child)

    def get_children(self):
        return self.children

    def sort_children(self):
        self.children.sort(key=lambda x: x.val, reverse=False)

'''
Just For Testing Purpose only
n=Node(4)
n1=Node(5)
n2=Node(6)
n3=Node(7)
n.add_children(n2)
n.add_children(n1)
n.add_children(n3)
n.sort_children()
print n

'''