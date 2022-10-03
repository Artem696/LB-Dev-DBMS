
class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.end = None
    def add_to_front(self, new_node):
        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def add_to_end(self, new_node):
        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            new_node.prev = self.end
            self.end = new_node
    def remove_first(self):
        if self.head is None:
            print("Error: List is empty")
    def remove_end(self):
        if self.head is None:
            print("Error: List is empty")
    def find_node(self,node):
        pass
if __name__ == '__main__':
    my_list = DoubleLinkedList()
    my_list.add_to_end(Node(1))
    my_list.add_to_end(Node(2))
    my_list.add_to_end(Node(3))
    print(my_list)
