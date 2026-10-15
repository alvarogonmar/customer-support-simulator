class Node:
    def __init__(self, ticket_id):
        self.ticket_id = ticket_id
        self.next = None

class TicketQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, ticket_id): # O(1)
        new_node = Node(ticket_id)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        
        temp = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return temp.ticket_id
    def peek(self):
        # Si la cola está vacía, devolver None
        if self.head is None:
            return None

        # Si tiene elementos, devolver el ticket_id de head
        return self.head.ticket_id

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

        