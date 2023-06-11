# Custom Node & Linked List Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lingkedlist:
    def __init__(self):
        self.head = None

# Menambah Elemen Linked List
    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Menghapus Elemen Linked List
    def remove_front(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # Mencetak Isi Linked List
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Membuat dan mencetak linked list
linked_list = Lingkedlist()
linked_list.add_to_front(3)
linked_list.add_to_front(2)
linked_list.add_to_front(1)

linked_list.add_to_end(4)
linked_list.add_to_end(5)
linked_list.add_to_end(6)

print("Linked list awal: ")
linked_list.print_linked_list()

# Menghapus dam mencetak linked list
linked_list.remove_front()
linked_list.remove_end()

print("Linked list setelah penghapusan: ")
linked_list.print_linked_list()
