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

def is_node_equal(node1,node2):
    return (node1 and node2 and node1.data==node2.data)

#iterative function to check if two trees are identical or not

def isIdentical(root1, root2):
    #if both tree are null return true
    if (not root1 and not root2):
        return True
    # if one of the child is None then return false
    if (not root1 and root2) or (root1 and not root2):
        return False
    #create a stack to hold the node pairs
    stack = [[root1,root2]]
    
    #loop till the stack is not empty
    while len(stack) > 0:
        node_array = stack.pop()
        node1 = node_array.pop()
        node2 = node_array.pop()
        #if both the values are not eqaul return False
        if not is_node_equal(node1,node2):
            return False
        #push left node pair if exists
        if node1.left and node2.left:
            stack.append([node1.left, node2.left])
        #if ony once exists then return false
        elif node1.left or node2.left:
            return False

        #push the right node pair 
        if node1.right and node2.right:
            stack.append([node1.right, node2.right])
        elif node1.right or node2.right:
            return False

    return True




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
    root2.left.right.left = Node(8)
    root2.left.right.left.left = Node(9)
    root2.left.right.left.left.left = Node(10)
    root2.right.right = Node(7)
    root2.right.right.right = Node(11)

    print("root1 and root are identical" if isIdentical(root1,root2) else "root 1 and root2 are not identical")
    root1.right.right.right = Node(13)
    print("root1 and root are identical" if isIdentical(root1,root2) else "root 1 and root2 are not identical")

