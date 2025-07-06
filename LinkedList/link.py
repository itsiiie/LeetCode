class Node:
    def __init__(self, data):
        self.data = data      # stores the value
        self.next = None      # stores reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None      # head of the linked list (starts empty)

    def insert_at_beginning(self, data):
        new_node = Node(data)      # create a new node
        new_node.next = self.head  # link it to the current head
        self.head = new_node       # move head to new node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
  
    

# 💡 Example Usage:
ll = LinkedList()
length = int(input("Entr the length:"))
for i in range(length):
    num = int(input("Enter the number:"))
    ll.insert_at_beginning(num)

ll.print_list()  # Output: 1 -> 5 -> 10 -> None
