from models.ticket import Ticket
from services.support_system import SupportSystem

system = SupportSystem()

ticket1 = Ticket(101, "Login problem", 2, "Technical")
ticket2 = Ticket(102, "Payment failed", 1, "Billing")
duplicate = Ticket(101, "Another problem", 3, "General")

print(system.add_ticket(ticket1))     # True
print(system.add_ticket(ticket2))     # True
print(system.add_ticket(duplicate))   # False

print(system.tickets.size)            # 2
print(system.pending_queue.size)      # 2

print(system.pending_queue.peek())    # 101
print(system.tickets.get(101).description)  # Login problem