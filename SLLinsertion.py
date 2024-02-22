class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self,):
        self.head= None

    def insert_beiginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    
    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def display(self,):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next


L = SingleLinkedList()
n = Node(10)
L.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
L.insert_beiginning(5)
L.insert_end(60)
L.insert_position(3,25)
L.display()