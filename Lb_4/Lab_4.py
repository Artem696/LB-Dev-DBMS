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
        current = elem.right
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
                if elem.parent.left.value == value:
                    elem.parent.left = elem.left
                elif elem.parent.right.value == value:
                    elem.parent.right = elem.left
            elif elem.right is not None:
                if elem.parent.left.value == value:
                    elem.parent.left = elem.right
                elif elem.parent.right.value == value:
                    elem.parent.right = elem.right
        # Есть и оба потомка 
        elif elem.left is not None and elem.right is not None:
            minn = self.find_min(elem)
            if elem.parent is None:
                self.value = minn.value
            elif elem.parent.left == elem:
                elem.parent.left.value = minn.value
            elif elem.parent.right == elem:
                elem.parent.right.value = minn.value
            if minn.left is None and minn.right is None:
                if minn.parent.left == minn:
                    minn.parent.left = None
                elif minn.parent.right == minn:
                    minn.parent.right = None
            else:
                minn.value = minn.right.value
                minn.right = None
                    
            #print(123456)
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
tree.insert(7)
tree.insert(17)
tree.insert(18)
#tree.insert(15)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.print()
tree.delete(7)
tree.print()