class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self,data):
        self.head = Node(data = data, next = self.head)
    
    def is_empty(self):
        return self.head == None
    
    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data = data)
            return
            curr = curr.next
            while curr.next:
                curr = curr.next
            curr.next = Node(data = data)
    
    def delete_node(self, key):
        curr = self.head
        prev = Node
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
    

    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data
    
    def print_list(self):
        Node = self.head
        while Node != None:
            print(Node.data)
            Node = Node.next


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()