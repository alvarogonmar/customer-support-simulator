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
    def process_next_ticket(self):
        # 1. Sacar el primer ticket_id de la Queue
        ticket_id = self.pending_queue.dequeue()

        # 2. Si la Queue estaba vacía, devolver None
        if ticket_id is None:
            return None

        # 3. Buscar el objeto Ticket en el Hash Map
        ticket = self.tickets.get(ticket_id)

        if ticket is None:
            return None
        # 4. Cambiar su status a "In Progress"
        ticket.status = "In Progress"

        # 5. Devolver el objeto Ticket
        return ticket
