from data_structures.ticket_queue import TicketQueue

queue = TicketQueue()

print(queue.is_empty())  # True
print(queue.peek())      # None

queue.enqueue(101)
queue.enqueue(102)
queue.enqueue(103)

print(queue.size)        # 3
print(queue.peek())      # 101

print(queue.dequeue())   # 101
print(queue.dequeue())   # 102
print(queue.dequeue())   # 103

print(queue.is_empty())  # True
print(queue.dequeue())   # None
print(queue.size)        # 0