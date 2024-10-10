
# Classe dels nodes d'una Linked List:
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Una Linked List és una classe amb un únic "Head Node":
class LinkedList:
    def __init__(self):
        self.head = None

    # Mètode per inserir elements en una Linked List
    def insert(self, data):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        else:
            self.head = Node(data)
    
    # Mètode per imprimir una Linked List
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Mètode per revertir una Linked List (MEU)
    def reverseList(self):
        current = self.head
        reverse = LinkedList()
        while current:
            reverse.head = Node(current.data, reverse.head)
            current = current.next
        return reverse

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert("hola")
LL.insert([1,2,3])
LL.insert({1:2, 2:3, 3:1})
LL.printList()

RLL = LL.reverseList()
RLL.printList()