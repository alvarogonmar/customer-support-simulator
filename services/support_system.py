from data_structures.ticket_hashmap import TicketHashMap
from data_structures.ticket_queue import TicketQueue


class SupportSystem:
    def __init__(self):
        self.tickets = TicketHashMap()
        self.pending_queue = TicketQueue()

    def add_ticket(self, ticket):
        # 1. Intentar insertar en el Hash Map
        inserted = self.tickets.insert(ticket)
        # 2. Si el ticket ya existe, devolver False
        # 3. Agregar ticket.id a la Queue
        if inserted:
            self.pending_queue.enqueue(ticket.id)
        else:
            return inserted

        # 4. Devolver True
        return True