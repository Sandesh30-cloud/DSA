class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self,value):
        newNode = Node(value) 
        newNode.next = self.head
        self.head = newNode

        self.n += 1

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end='->')
            curr = curr.next
            

    def append(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.n += 1
            return 
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = newNode
        self.n += 1


    def insert_after(self,after,value):
        newNode = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            newNode.next = curr.next
            curr.next = newNode
        else: return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty Linked List'
        self.head = self.head.next
        self.n -= 1
        
    def pop(self):
        if self.head == None:
            return 'Its already Empty'
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1


    def remove(self,value):
        if self.head == None:
            return 'Empty Linked List'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            return 'Not found'
        else:
            curr.next = curr.next.next

    def search(self,value):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos += 1
        return 'Not Found'

    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return 'Not Found'

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
