
class Node:
    
    def __init__(self, value, parent):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def setValue(self, value):
        self.value = value

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setParent(self, parent):
        self.parent = parent


class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value, None)
        # If the tree is empty, create a root node
        if self.root == None:
            self.root = new_node
            
        else:
            current_node = self.root
            # While we don't reach a terminal node
            while current_node != None:
                parent_node = current_node

                # If node value is less than that of the current node, go left
                if new_node.getValue() < current_node.getValue():
                    current_node = current_node.getLeft()
                # Else, go right
                else:
                    current_node = current_node.getRight()

            # Insert the node as a terminal node
            if new_node.getValue() < parent_node.getValue():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)

            # Set the parent node to be the new node
            new_node.setParent(parent_node)

                
