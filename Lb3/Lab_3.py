
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
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    def add_to_end(self, new_node):
        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            new_node.prev = self.end
            self.end = new_node
    def remove_first(self):
        if self.head is None:
            print("Error: List is empty")
        elif self.head.next == None:
            self.head = None
            self.end = None
        else:
            self.head = self.head.next
            self.head.prev = None
    def remove_end(self):
        if self.head is None:
            print("Error: List is empty")
        elif self.head.next == None:
            self.head = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None
    def find_node(self,node):
        current = self.head
        while current is not None:
            if current.value == node:
                return True
            else:
                current = current.next
        return False
    def remove_by_key(self,key):
        current = self.head
        while current is not None:
            if current.value == key:
                if current.prev == None:
                    current = current.next
                    self.head = current
                    if self.head is not None:
                        self.head.prev = None
                        return
                if current.next == None:
                    current = current.prev
                    self.end = current
                    self.end.next = None
                    return
                else:
                    current.prev.next = current.next
                    current = current.next
                    return
            else:
                current = current.next      
        return False
    def list_print(self):
        current = self.head
        print("DOUBLE LINKED LIST")
        print("-----")
        i = 0
        while current is not None:
            print (str(i) + ": " + str(current.value))
            i += 1
            current = current.next
        print("-----")
if __name__ == '__main__':
    my_list = DoubleLinkedList()
    my_list.add_to_end(Node(1))
    my_list.add_to_end(Node(2))
    my_list.add_to_end(Node(3))
    print(my_list.find_node(5))
    my_list.list_print()
    my_list.remove_by_key(2)
    my_list.list_print()
