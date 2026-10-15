from models.ticket import Ticket
from services.support_system import SupportSystem

system = SupportSystem()

system.add_ticket(Ticket(101, "Login problem", 2, "Technical"))
system.add_ticket(Ticket(102, "Payment failed", 1, "Billing"))

ticket = system.process_next_ticket()

print(ticket.id)
print(ticket.status)
print(system.pending_queue.peek())
print(system.pending_queue.size)

second_ticket = system.tickets.get(102)
print(second_ticket.status)