from hashlib import new


class BinatyTreeNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
    def insert(self, value):
        if self.value is None:
            self.value = value
            return

        current = self
        while True:
            if current.value > value:
                if current.left is None:
                    new_node = BinatyTreeNode(value)
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            elif current.value < value:
                if current.right is None:
                    new_node = BinatyTreeNode(value)
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
            elif current.value == value:
                print(f"value {value} already exists")
                break
    def find(self,value):
        if self.value is None:
            print("Tree is empty")
            return

        current = self
        while True:
            if current.value == value:
                print("Value found")
                return current
            elif current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                print("Value not found")
    def find_min(self,elem):
        current = elem
        while True:
            if current.left == None:
                return current
            current = current.left

    def delete(self,value):
        elem = self.find(value)
        if elem is None:
            print("Элемент не найден")
            return
        # Нет потомков
        if elem.left is None and elem.right is None:
            if elem.parent.left.value == value:
                elem.parent.left = None
            elif elem.parent.right.value == value:
                elem.parent.right = None
        # Есть левый или правый потомок
        elif elem.left is None or elem.right is None:
            if elem.left is not None:
                elem = elem.left
            elif elem.right is not None:
                elem = elem.right
        # Есть и оба потомка 
        elif elem.left is not None and elem.right is not None:
            pass
        minn = self.find_min(elem)
    def print(self,elem=None):
        current = self
        if elem is not None:
            current = elem
        print(current.value)
        if self.left:
            self.left.print(current.left)
        if self.right:
            self.right.print(current.right)


tree = BinatyTreeNode()
tree.insert(5)
tree.insert(17)
tree.insert(11)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.delete(6)
tree.print()
# tree.delete(4)
# print(tree.value)
# print(tree.left.value)
# print(tree.right.value)
# print(tree.left.left.value)
# print(tree.left.right.value)