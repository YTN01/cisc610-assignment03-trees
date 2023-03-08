#! /usr/bin/env python3

import csv

class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child


    def get_node_with_parent(self, data): 
        parent = None 
        current = self.root_node 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left_child 
            else: 
                parent = current 
                current = current.right_child 

        return (parent, current)

    def _leaf_nodes_count(self, current_node):
        if current_node is None:
            return 0
        else:
            if current_node.left_child is None and current_node.right_child is None:
                return 1
            return self._leaf_nodes_count(current_node.left_child) + self._leaf_nodes_count(current_node.right_child)

    def leaf_nodes_count(self):
        return self._leaf_nodes_count(self.root_node)

    def _height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self._height(root.left_child), self._height(root.right_child))

    def height(self):
        return self._height(self.root_node)


# n1 = Node("root node")
# n2 = Node("left child node")
# n3 = Node("right child node")
# n4 = Node("left grandchild node")
#
# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4
#
# current = n1
# while current:
#     print(current.data)
#     current = current.left_child
#
# tree = Tree()
# tree.insert(5)
# tree.insert(2)
# tree.insert(7)
# tree.insert(9)
# tree.insert(1)

# for i in range(1, 10):
#     found = tree.search(i)
#     print("{}: {}".format(i, found))


# solution code

if __name__ == '__main__':  # Main method
    tree = Tree()
    with open('./random_numbers.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for number in row:
                tree.insert(number)
    print('leaf nodes count: {0}'.format(tree.leaf_nodes_count()))
    print('tree height: {0}'.format(tree.height()))
