from models.ticket import Ticket
from data_structures.ticket_hashmap import TicketHashMap

hashmap = TicketHashMap(10)

for i in range(1, 11):
    ticket = Ticket(i, f"Problem {i}", 2, "Technical")
    hashmap.insert(ticket)

    print(
        f"Ticket: {i} | "
        f"Size: {hashmap.size} | "
        f"Capacity: {hashmap.capacity} | "
        f"Load Factor: {hashmap.get_load_factor():.2f}"
    )

for i in range(1, 11):
    ticket = hashmap.get(i)
    assert ticket is not None
    assert ticket.id == i

print("All tickets found successfully!")