from data_structures.ticket_hashmap import TicketHashMap
from data_structures.ticket_queue import TicketQueue


class SupportSystem:
    def __init__(self):
        self.tickets = TicketHashMap()
        self.pending_queue = TicketQueue()