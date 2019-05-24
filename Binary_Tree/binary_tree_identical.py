#code to find out is the binary trees are identical or not.


#A binary tree node
class Node:

    #constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)




if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.right.left = Node(8)
    root1.left.right.left.left = Node(9)
    root1.left.right.left.left.left = Node(10)
    root1.right.right = Node(7)
    root1.right.right.right = Node(11)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
